# feedbacktool

A full-stack feedback management system built with **Django REST Framework** (Backend) and **React.js** (Frontend).

---

## 🚀 Features

- User Registration and Login
- Role-based Access (Admin, Employee)
- Submit and Track Feedback
- Acknowledge Responses
- Dashboard for Teams
- JWT Authentication
- Dockerized Backend

---

## 📦 Tech Stack

- Backend: Django, Django REST Framework
- Frontend: React.js
- Database: SQLite (Dev) / MySQL (Prod)
- Authentication: JWT
- Docker: Backend containerization

---

## 🛠️ Setup Instructions

### Backend

```bash
cd feedbacktool
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Frontend
bash
Copy
Edit
cd feedback-frontend
npm install
npm start
🐳 Docker (Backend)
bash
Copy
Edit
docker build -t feedback-backend .
docker run -p 8000:8000 feedback-backend
📁 Folder Structure
bash
Copy
Edit
feedbacktool/
├── feedbacktool_project/       # Django project
├── core/                       # Django app
├── feedback-frontend/          # React app
├── Dockerfile
├── manage.py
└── README.md
🙋‍♂️ Author
Ranganath B
GitHub

yaml
Copy
Edit

---

2. ### **Commit and Push `README.md`**

```bash
git add README.md
git commit -m "Added README.md with project overview"
git push
