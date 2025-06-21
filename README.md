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

### ⚙️ Backend


- cd feedbacktool
- python -m venv venv
- venv\Scripts\activate   # For Windows
# OR
- source venv/bin/activate   # For Mac/Linux

- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

---

###🌐 Frontend

- cd feedback-frontend
- npm install
- npm start

###🐳 Docker (Backend Only)
- bash
- Copy
- Edit
# Build the Docker image
- docker build -t feedbacktool-backend .

# Run the Docker container
- docker run -p 8000:8000 feedbacktool-backend


## 📐 Design Decisions
- Modular Django App (core): Keeps business logic and views clean and maintainable.

- Token-based Authentication: Secure user access for admins and employees.

- Role-based UI: Separate dashboard for Admins (acknowledge feedback) and Employees (submit feedback).

- RESTful APIs: Built using DRF for scalability and frontend integration.

- Frontend Routing: Built with React Router DOM for SPA feel.

📁 Folder Structure

- feedbacktool/
- ├── feedbacktool_project/       # Django project
- ├── core/                       # Django app
- ├── feedback-frontend/          # React app
- ├── Dockerfile
- ├── manage.py
- └── README.md
  
### 🙋‍♂️ Author
- Sri Ranganath B
- GitHub

2. ### **Commit and Push `README.md`**

```bash
git add README.md
git commit -m "Added README.md with project overview"
git push
