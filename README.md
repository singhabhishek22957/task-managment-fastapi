# 🚀 Task Management System

A modern, secure, and production-oriented **full-stack Task Management application** built with **FastAPI, MongoDB, PyMongo Async, Streamlit, JWT Authentication, Pydantic, and Argon2**.

The project is divided into two independent applications:

* ⚡ **FastAPI** — REST API backend
* 🎨 **Streamlit** — frontend application

The backend follows a layered architecture separating **routes, controllers, services, middleware, schemas, models, and database operations**, while the Streamlit frontend communicates with the backend through HTTP APIs.

---

## ✨ Features

### 🔐 Authentication

* User registration
* User login
* JWT-based authentication
* Bearer token authentication
* Protected API routes
* Argon2 password hashing
* Authentication middleware
* User account validation

### 👤 User Management

* Get authenticated user
* Get users
* Get user by ID
* Update user
* Delete user
* User-specific data access

### 📝 Task Management

* Create tasks
* Fetch all user tasks
* Fetch task by slug
* Update task status
* Update task priority
* Edit task details
* Soft delete tasks
* Task ownership
* Unique task slugs
* Task timestamps
* Task status management
* Task priority management

### 🎨 Streamlit Frontend

* Login interface
* Registration interface
* Dashboard
* Task listing
* Task table
* Task creation
* Task editing
* Status editing
* Priority editing
* Task deletion
* API integration
* Authentication state management
* User-specific task display

### 🛡️ Backend

* Layered architecture
* Async MongoDB operations
* Pydantic validation
* Centralized exception handling
* Standardized API responses
* MongoDB indexes
* JWT authentication
* Protected routes
* Swagger/OpenAPI documentation

---

# 🏗️ Full-Stack Architecture

```text
┌──────────────────────────────────────────────┐
│              Streamlit Frontend              │
│                                              │
│  Login │ Register │ Dashboard │ Tasks        │
│                                              │
│              HTTP Requests                   │
└──────────────────────┬───────────────────────┘
                       │
                       │ REST API
                       ▼
┌──────────────────────────────────────────────┐
│                FastAPI Backend               │
│                                              │
│  Middleware                                  │
│       ↓                                      │
│  Routes                                      │
│       ↓                                      │
│  Controllers                                 │
│       ↓                                      │
│  Services                                    │
│       ↓                                      │
│  MongoDB                                     │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     MongoDB     │
              │                 │
              │ Users           │
              │ Tasks           │
              └─────────────────┘
```

---

# 📁 Project Structure

```text
task-management/
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── db.py
│   │   │   ├── security.py
│   │   │   ├── exceptions.py
│   │   │   └── utils.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── auth.py
│   │   │   ├── task.py
│   │   │   └── common.py
│   │   │
│   │   ├── middleware/
│   │   │   └── auth.py
│   │   │
│   │   ├── controller/
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   └── handlers/
│   │       └── exceptions.py
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   ├── test_tasks.py
│   │   └── conftest.py
│   │
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   │
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── dashboard.py
│   │   ├── tasks.py
│   │   └── edit_task.py
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── task_table.py
│   │   └── task_form.py
│   │
│   ├── services/
│   │   ├── api.py
│   │   ├── auth.py
│   │   └── task.py
│   │
│   ├── utils/
│   │   ├── session.py
│   │   └── helpers.py
│   │
│   ├── .streamlit/
│   │   └── config.toml
│   │
│   ├── .env
│   ├── .env.example
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

## Backend

| Technology            | Purpose                     |
| --------------------- | --------------------------- |
| **Python**            | Programming language        |
| **FastAPI**           | REST API framework          |
| **MongoDB**           | NoSQL database              |
| **PyMongo Async**     | Async MongoDB operations    |
| **Pydantic**          | Request/response validation |
| **JWT**               | Authentication              |
| **Argon2**            | Password hashing            |
| **Uvicorn**           | ASGI server                 |
| **Swagger / OpenAPI** | API documentation           |

## Frontend

| Technology                 | Purpose                     |
| -------------------------- | --------------------------- |
| **Python**                 | Programming language        |
| **Streamlit**              | Frontend/UI framework       |
| **Requests / HTTP Client** | API communication           |
| **Session State**          | Authentication and UI state |
| **dotenv**                 | Environment configuration   |

---

# 🔄 Application Request Flow

When a user performs an action from Streamlit:

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Frontend Service
 │
 ▼
HTTP Request
 │
 ▼
FastAPI
 │
 ▼
Authentication Middleware
 │
 ▼
Route
 │
 ▼
Controller
 │
 ▼
Service
 │
 ▼
MongoDB
 │
 ▼
FastAPI Response
 │
 ▼
Streamlit
 │
 ▼
UI Update
```

---

# 🔐 Authentication Flow

```text
┌───────────────┐
│    Register   │
└───────┬───────┘
        │
        ▼
Validate Input
        │
        ▼
Hash Password
        │
        ▼
MongoDB
```

Login:

```text
┌───────────────┐
│     Login     │
└───────┬───────┘
        │
        ▼
Find User
        │
        ▼
Verify Argon2 Password
        │
        ▼
Generate JWT
        │
        ▼
Return Access Token
        │
        ▼
Streamlit Session State
```

Protected request:

```text
Streamlit
    │
    ▼
Authorization: Bearer <token>
    │
    ▼
FastAPI Middleware
    │
    ▼
Validate JWT
    │
    ▼
Get User ID
    │
    ▼
Find User
    │
    ▼
request.state.user
    │
    ▼
Protected Route
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/task-management.git

cd task-management
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

## Create Virtual Environment

### Windows

```powershell
python -m venv myvenv
```

Activate:

```powershell
myvenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv myvenv
```

Activate:

```bash
source myvenv/bin/activate
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Backend Environment Variables

Create:

```text
backend/.env
```

Example:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=task_management

JWT_SECRET_KEY=your-long-random-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate a secure JWT secret:

```python
import secrets

print(secrets.token_urlsafe(32))
```

Never commit `.env` to Git.

---

# 🍃 MongoDB

The application uses MongoDB for persistent storage.

### Local MongoDB

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=task_management
```

### MongoDB Atlas

Use your Atlas connection string:

```env
MONGODB_URL=mongodb+srv://<username>:<password>@<cluster>/<database>
DATABASE_NAME=task_management
```

The application creates required indexes during startup.

---

# ▶️ Run FastAPI Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

# 📚 FastAPI Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Swagger provides an interactive interface for testing the API.

---

# 🎨 Streamlit Frontend Setup

Open another terminal.

Navigate to the frontend:

```bash
cd frontend
```

Create a virtual environment:

```powershell
python -m venv myvenv
```

Activate:

```powershell
myvenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Frontend Environment Variables

Create:

```text
frontend/.env
```

Example:

```env
API_BASE_URL=http://127.0.0.1:8000
```

The Streamlit frontend uses this URL to communicate with FastAPI.

---

# ▶️ Run Streamlit

From the `frontend` directory:

```bash
streamlit run app.py
```

The frontend will normally be available at:

```text
http://localhost:8501
```

---

# 🔗 Running Full Application

You need two terminals.

### Terminal 1 — FastAPI

```bash
cd backend

myvenv\Scripts\activate

uvicorn app.main:app --reload
```

### Terminal 2 — Streamlit

```bash
cd frontend

myvenv\Scripts\activate

streamlit run app.py
```

Application:

```text
Frontend
http://localhost:8501

Backend
http://127.0.0.1:8000

Swagger
http://127.0.0.1:8000/docs
```

---

# 🔐 Authentication

The application uses:

```text
JWT + Bearer Authentication
```

After successful login:

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
  }
}
```

The frontend stores the authentication state and sends the JWT with protected API requests.

```http
Authorization: Bearer <access_token>
```

---

# 🛣️ API Routes

## 🔐 Authentication

Base URL:

```text
/auth
```

### Register

```http
POST /auth/register
```

Example:

```json
{
  "name": "Abhishek",
  "email": "abhi@example.com",
  "password": "password123"
}
```

### Login

```http
POST /auth/login
```

Example:

```json
{
  "email": "abhi@example.com",
  "password": "password123"
}
```

---

# 👤 User Routes

Base URL:

```text
/users
```

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/users/`          | Get users                 |
| GET    | `/users/{user_id}` | Get user                  |
| PUT    | `/users/{user_id}` | Update user               |
| DELETE | `/users/`          | Delete authenticated user |

Protected routes require a valid JWT.

---

# 📝 Task Routes

Base URL:

```text
/task
```

| Method | Endpoint              | Description                    |
| ------ | --------------------- | ------------------------------ |
| POST   | `/task/`              | Create task                    |
| GET    | `/task/all`           | Get authenticated user's tasks |
| GET    | `/task/{slug}`        | Get task                       |
| PATCH  | `/task/{slug}/status` | Update task status             |
| DELETE | `/task/{slug}`        | Soft delete task               |

---

# 📋 Task Example

Create task:

```http
POST /task/
```

Request:

```json
{
  "title": "Learn FastAPI",
  "description": "Learn production FastAPI architecture",
  "status": "pending",
  "priority": "medium",
  "due_date": null
}
```

The backend generates a slug:

```text
Learn FastAPI
      ↓
learn-fastapi
```

Example document:

```json
{
  "user_id": "64...",
  "title": "Learn FastAPI",
  "slug": "learn-fastapi",
  "description": "Learn production FastAPI architecture",
  "status": "pending",
  "priority": "medium",
  "is_deleted": false,
  "due_date": null,
  "created_at": "2026-09-28T17:25:52",
  "updated_at": "2026-09-28T17:25:52",
  "completed_at": null
}
```

---

# 👥 Task Ownership

Every task belongs to a user:

```json
{
  "user_id": "64..."
}
```

When fetching tasks, the backend filters using the authenticated user's ID:

```python
{
    "user_id": user_id,
    "is_deleted": False
}
```

Therefore:

```text
User A
 ├── Task 1
 ├── Task 2
 └── Task 3

User B
 ├── Task 4
 └── Task 5
```

User A cannot access User B's tasks.

---

# 🗑️ Soft Delete

Tasks are not permanently removed from MongoDB.

Instead:

```python
{
    "$set": {
        "is_deleted": True
    }
}
```

Normal task queries only return:

```python
{
    "is_deleted": False
}
```

This preserves the original database record.

---

# 🎨 Streamlit Application

The Streamlit frontend provides the user interface for interacting with the FastAPI backend.

Typical flow:

```text
Login
  │
  ▼
Dashboard
  │
  ├── Create Task
  │
  ├── View Tasks
  │
  ├── Edit Task
  │
  ├── Update Status
  │
  ├── Update Priority
  │
  └── Delete Task
```

The frontend does not directly communicate with MongoDB.

```text
Streamlit
    │
    │ HTTP
    ▼
FastAPI
    │
    │ Async Database Operations
    ▼
MongoDB
```

This separation keeps the frontend independent from database implementation details.

---

# 📦 Standard API Response

Successful response:

```json
{
  "success": true,
  "message": "Operation successful",
  "data": {}
}
```

Error response:

```json
{
  "success": false,
  "message": "Task not found",
  "error": {
    "code": "TASK_NOT_FOUND"
  }
}
```

A consistent response format makes API consumption easier for the Streamlit frontend.

---

# ❌ Error Handling

Application exceptions are handled centrally.

Examples:

```text
USER_NOT_FOUND
USER_ALREADY_EXISTS
INVALID_CREDENTIALS
UNAUTHORIZED
TASK_NOT_FOUND
TASK_ALREADY_EXISTS
```

Instead of implementing error responses independently inside every route, centralized exception handlers convert application exceptions into consistent HTTP responses.

---

# 🛡️ Security

The project implements several security practices:

* JWT authentication
* Bearer token authorization
* Argon2 password hashing
* Protected API routes
* User-specific task queries
* Environment-based secrets
* Input validation with Pydantic
* Centralized exception handling
* MongoDB unique indexes
* Soft deletion

Passwords are never stored as plaintext.

```text
Plain Password
      ↓
    Argon2
      ↓
Password Hash
      ↓
   MongoDB
```

---

# 🗄️ MongoDB Indexes

Indexes are used for commonly queried fields.

Examples:

```text
users.email
tasks.slug
tasks.user_id
tasks.user_id + tasks.status
```

Example unique index:

```python
await task_collection.create_index(
    [("slug", ASCENDING)],
    unique=True,
    name="unique_task_slug"
)
```

---

# 🧪 Testing

Tests can be executed using:

```bash
pytest
```

Recommended structure:

```text
tests/
├── test_auth.py
├── test_users.py
├── test_tasks.py
└── conftest.py
```

Important test cases:

* User registration
* Duplicate email
* Login
* Invalid password
* Missing JWT
* Invalid JWT
* Expired JWT
* Create task
* Fetch tasks
* Update task
* Delete task
* Task ownership
* User task isolation

---

# 📌 HTTP Status Codes

| Status | Meaning                         |
| ------ | ------------------------------- |
| `200`  | Successful request              |
| `201`  | Resource created                |
| `400`  | Bad request                     |
| `401`  | Authentication required/invalid |
| `403`  | Access forbidden                |
| `404`  | Resource not found              |
| `409`  | Resource conflict               |
| `422`  | Validation error                |
| `500`  | Internal server error           |

---

# 🚀 Future Improvements

### Authentication

* [ ] Refresh tokens
* [ ] Email verification
* [ ] Password reset
* [ ] Role-based authorization

### Task Management

* [ ] Pagination
* [ ] Task filtering
* [ ] Task sorting
* [ ] Task search
* [ ] Task categories
* [ ] Task labels
* [ ] Task deadlines and reminders

### Backend

* [ ] Rate limiting
* [ ] Redis caching
* [ ] Background jobs
* [ ] Automated tests
* [ ] API versioning
* [ ] Production logging
* [ ] Docker
* [ ] CI/CD

### Frontend

* [ ] Advanced dashboard
* [ ] Task analytics
* [ ] Search and filters
* [ ] Pagination
* [ ] Better error notifications
* [ ] Loading states
* [ ] User profile
* [ ] Responsive UI improvements

---

# 🧑‍💻 Development Commands

## Backend

```bash
cd backend
```

Activate environment:

```powershell
myvenv\Scripts\activate
```

Run:

```bash
uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend
```

Activate environment:

```powershell
myvenv\Scripts\activate
```

Run:

```bash
streamlit run app.py
```

---

# 🌐 Application URLs

| Application           | URL                           |
| --------------------- | ----------------------------- |
| Streamlit Frontend    | `http://localhost:8501`       |
| FastAPI Backend       | `http://127.0.0.1:8000`       |
| Swagger Documentation | `http://127.0.0.1:8000/docs`  |
| ReDoc                 | `http://127.0.0.1:8000/redoc` |

---

# 📄 License

This project is available for educational and development purposes.

---

# 🎯 Project Goal

The primary goal of this project is to understand how a **modern full-stack Python application** can be designed by separating the frontend, backend, database, authentication, and business logic.

```text
                 Task Management
                       │
          ┌────────────┴────────────┐
          │                         │
      Streamlit                  FastAPI
      Frontend                   Backend
          │                         │
          │                         ├── JWT
          │                         ├── Middleware
          │                         ├── Pydantic
          │                         ├── Services
          │                         ├── Controllers
          │                         └── REST API
          │
          └────────────┬────────────┘
                       │
                    MongoDB
                       │
                PyMongo Async
```

This project provides practical experience with:

```text
Python
   +
Streamlit
   +
FastAPI
   +
MongoDB
   +
Async Programming
   +
JWT Authentication
   +
Argon2
   +
Pydantic
   +
REST API Design
   +
Layered Architecture
   +
Frontend / Backend Separation
```

---

## ⭐ Built With

**FastAPI + MongoDB + Streamlit + Python**

Built for learning, experimentation, and production-oriented backend/frontend architecture.
