# Authentication Web App (Flask + SQLAlchemy)

A full-stack authentication web application built with **Flask**, featuring secure user registration, login/logout, session management, and user-specific data storage using **SQLAlchemy** and **Flask-Login**.

This project demonstrates backend authentication logic, database modeling, and server-rendered HTML templates.

---

## 🚀 Features

- User registration with email, name, and password
- Secure password hashing using Werkzeug (`scrypt`)
- User login and logout with session persistence
- Authentication-protected routes
- User-specific notes (create & delete)
- SQLite database with SQLAlchemy ORM
- Server-side form validation and flash messages

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite

**Frontend**
- HTML (Jinja2 templates)
- CSS (custom styling)

**Security**
- Password hashing with `generate_password_hash`
- Login session management
- Access control using `@login_required`

---

## 🔐 Authentication Flow

1. Users sign up with email, name, and password
2. Passwords are securely hashed before storage
3. Users log in using email and password
4. Flask-Login manages user sessions
5. Protected routes require authentication
6. Logged-in users can create and delete personal notes

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Zeuz6/authentication-web-app.git
cd authentication-web-app

pip install flask flask-login flask-sqlalchemy
python main.py
http://127.0.0.1:5000
