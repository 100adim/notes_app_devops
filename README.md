# Notes App with Flask, Redis and Docker

This project implements a simple notes management service using **Flask** (Python), **Redis**, and **Docker Compose**.
This project was created as part of a Devops assignment

## 🧩 Features

- Add a note (`POST /note`)
- View all notes (`GET /notes`)
- Delete a note (`DELETE /note/<id>`)
- Notes are stored in Redis and persist using Docker volumes

---

## 🐳 Technologies Used

- **Flask** – web framework (Python)
- **Redis** – in-memory database for storing notes
- **Docker** – for containerization
- **Docker Compose** – to orchestrate the service and Redis

---

## 🚀 How to Run the Project

Make sure Docker and Docker Compose are installed.

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd notes_app_devops
