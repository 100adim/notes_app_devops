# Notes App with Flask, Redis and Docker

This project was created as part of a DevOps assignment.  
הוא כולל שירות פשוט לניהול פתקים באמצעות **Flask**, שימוש ב־**Redis** לשמירה של המידע, ו־**Docker Compose** לניהול הרצת המערכת.

## 🧩 Features

- הוספת פתק חדש (`POST /note`)
- הצגת כל הפתקים (`GET /notes`)
- מחיקת פתק לפי מזהה (`DELETE /note/<id>`)
- הפתקים נשמרים ב־Redis ונשמרים גם אחרי כיבוי באמצעות Docker volumes

---

## 🐳 Technologies Used

- **Flask** – פריימוורק לפייתון לבניית שירותים
- **Redis** – מסד נתונים בזיכרון לשמירת הפתקים
- **Docker** – להרצת המערכת בתוך קונטיינרים
- **Docker Compose** – לחיבור בין השירותים השונים

---

## 🚀 How to Run the Project

כדי להריץ את הפרויקט, צריך ש־Docker ו־Docker Compose יהיו מותקנים.

1. שיבוט של הריפו:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd notes_app_devops
