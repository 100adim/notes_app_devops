# Notes App with Flask, Redis and Docker

This is a simple notes app we built as part of a DevOps assignment.  
It uses **Flask** for the backend, **Redis** to store the notes, and **Docker Compose** to run everything together easily.

---

## 🧩 Features

- Add a new note (`POST /note`)
- View all notes (`GET /notes`)
- Delete a note by ID (`DELETE /note/<id>`)
- Notes are stored in Redis and persist using Docker volumes

---

## 🐳 Technologies Used

- **Flask** – lightweight Python web framework  
- **Redis** – fast in-memory key-value store  
- **Docker** – to run the app in containers  
- **Docker Compose** – to manage and connect the services

---

## 🚀 How to Run the Project

Make sure you have Docker and Docker Compose installed.

1. Clone this repository:
```bash
git clone https://github.com/100adim/notes_app_devops.git
cd notes_app_devops
