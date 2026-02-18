# 🏫 School Management System API

## 📌 Project Overview

The **School Management System API** is a backend application built with
**Django** and **Django REST Framework (DRF)** to manage core academic
operations of a school. It provides RESTful endpoints for managing
students, teachers, classes, subjects, and schedules.

This project demonstrates real‑world backend development practices
including authentication, role‑based access control, relational database
modeling, and API design.

---

## 🚀 Features

### ✅ Core Features

- User authentication and authorization (JWT)
- Student management
- Teacher management
- Class management
- Subject management
- Class scheduling

### ⚙️ Functional Capabilities

- Create, update, delete, and retrieve students
- Create, update, delete, and retrieve teachers
- Assign teachers to classes
- Assign subjects to teachers
- Manage class schedules
- View schedules by class or teacher

### ⭐ Optional Advanced Features

- Role‑based permissions (Admin, Teacher, Student)
- Pagination and filtering
- API documentation (Swagger)
- Deployment support

---

## 🛠️ Tech Stack

Technology Purpose

---

Django Backend framework
Django REST Framework API development
SQLite / PostgreSQL Database
JWT Authentication Secure login
Git & GitHub Version control
PythonAnywhere / Heroku Deployment

---

## 📂 Project Structure

    school_management_api/
    │
    ├── accounts/      # Custom user & authentication
    ├── students/      # Student management
    ├── teachers/      # Teacher management
    ├── academics/     # Classes, subjects, schedules
    ├── config/        # Project settings
    └── manage.py

---

## 🧠 Database Models

### User

- username
- email
- password
- role (Admin / Teacher / Student)

### Student

- user (One‑to‑One)
- registration number
- assigned class

### Teacher

- user (One‑to‑One)
- staff ID

### ClassRoom

- name
- level
- class teacher

### Subject

- teacher
- name
- code

### Schedule

- class
- subject
- teacher
- day of week
- start & end time

---

## 🔐 Authentication Endpoints

Method Endpoint Description

---

POST /api/auth/register/ Register user
POST /api/auth/login/ Login user

---

## 🎓 Student Endpoints

Method Endpoint

---

GET /api/students/
POST /api/students/
GET /api/students/{id}/
PUT /api/students/{id}/
DELETE /api/students/{id}/

---

## 👩‍🏫 Teacher Endpoints

Method Endpoint

---

GET /api/teachers/
POST /api/teachers/
GET /api/teachers/{id}/
PUT /api/teachers/{id}/
DELETE /api/teachers/{id}/

---

## 📚 Class & Subject Endpoints

Method Endpoint

---

GET /api/classes/
POST /api/classes/
GET /api/subjects/
POST /api/subjects/

---

## 📅 Schedule Endpoints

Method Endpoint

---

GET /api/schedules/
POST /api/schedules/
GET /api/schedules/class/{id}/
GET /api/schedules/teacher/{id}/

---

## ⚡ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd school_management_api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start Server

```bash
python manage.py runserver
```

---

## 🧪 Testing API

You can test endpoints using: - Postman - Insomnia - DRF Browsable API

---

## 🚀 Deployment Options

- PythonAnywhere
- Heroku
- Render

---

## 👨‍💻 Author

**Bitrus Dauda Gana**

---

## 📜 License

This project is for educational purposes.
