FROM python:3.10-slim

WORKDIR /app
# Could be done in one copy line
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# you copy more files than you need to because your repo not organized enough
COPY . . 

CMD ["python", "app.py"]
