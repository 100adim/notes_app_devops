from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)


def get_next_id():
    return r.incr("next_note_id")

@app.route('/note', methods=['POST'])
def add_note():
    data = request.json
    text = data.get('text')
    tag = data.get('tag')

    if not text or not tag:
        return jsonify({'error': 'Missing text or tag'}), 400

    note_id = get_next_id()
    note_key = f'note:{note_id}'

    note_data = {
        'id': note_id,
        'text': text,
        'tag': tag
    }

    r.set(note_key, json.dumps(note_data))
    r.sadd(f'tag:{tag}', note_id)

    return jsonify({'message': 'Note added', 'id': note_id}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    tag_filter = request.args.get('tag')
    notes = []

    if tag_filter:
        note_ids = r.smembers(f'tag:{tag_filter}')
    else:
        note_keys = r.keys('note:*')
        note_ids = [key.split(':')[1] for key in note_keys]

    for nid in note_ids:
        note_json = r.get(f'note:{nid}')
        if note_json:
            notes.append(json.loads(note_json))

    return jsonify(notes), 200

def delete_note(note_id):
    note_key = f'note:{note_id}'
    note_json = r.get(note_key)

    if not note_json:
        return jsonify({'error': 'Note not found'}), 404

    note_data = json.loads(note_json)
    r.delete(note_key)
    r.srem(f'tag:{note_data["tag"]}', note_id)

    return jsonify({'message': 'Note deleted'}), 200

                  
@app.route("/about")
def about():
    return {"message": "This is part of Adi & Roni's Devops project"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
