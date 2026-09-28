# 🚀 Task Management API

A modern, secure, and production-oriented **Task Management REST API** built with **FastAPI, MongoDB, PyMongo Async, JWT Authentication, and Argon2 password hashing**.

The project follows a layered backend architecture separating **routes, controllers, services, middleware, schemas, models, and database operations**.

---

## ✨ Features

* 🔐 JWT-based authentication
* 🔑 Argon2 password hashing
* 👤 User registration and login
* 🛡️ Authentication middleware
* 📋 Task CRUD operations
* 👥 User-specific task access
* 🗑️ Soft delete support
* 🔎 Unique task slugs
* ⚡ Asynchronous MongoDB operations
* ✅ Pydantic request/response validation
* 🧱 Centralized exception handling
* 📦 Standardized API responses
* 📚 Automatic Swagger/OpenAPI documentation
* 🔒 Protected API routes
* 🕒 Task timestamps
* 🎯 Task status and priority management

---

## 🛠️ Tech Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| **Python**            | Programming language |
| **FastAPI**           | REST API framework   |
| **MongoDB**           | Database             |
| **PyMongo Async**     | Async MongoDB driver |
| **Pydantic**          | Data validation      |
| **JWT**               | Authentication       |
| **Argon2**            | Password hashing     |
| **Uvicorn**           | ASGI server          |
| **Swagger / OpenAPI** | API documentation    |

---

# 🏗️ Project Architecture

```text
task-management-api/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── task.py
│   │   └── common.py
│   │
│   ├── middleware/
│   │   └── auth.py
│   │
│   ├── controller/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── task.py
│   │
│   └── handlers/
│       └── exceptions.py
│
├── tests/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔄 Request Flow

The application follows a layered request flow:

```text
                    HTTP Request
                         │
                         ▼
                ┌─────────────────┐
                │ Auth Middleware │
                └────────┬────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │    Routes   │
                  └──────┬──────┘
                         │
                         ▼
                ┌────────────────┐
                │   Controller   │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    Service     │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    MongoDB     │
                └────────────────┘
```

### Responsibilities

**Middleware**

Handles authentication and validates the JWT token.

**Routes**

Handle HTTP concerns such as:

* URL
* HTTP method
* request parameters
* response model
* status code

**Controllers**

Coordinate the request and prepare data for services.

**Services**

Contain business logic and database operations.

**Models**

Create MongoDB document structures.

**Schemas**

Validate incoming and outgoing API data.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/task-management-api.git

cd task-management-api
```

## 2. Create virtual environment

### Windows

```powershell
python -m venv myvenv
```

Activate it:

```powershell
myvenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv myvenv

source myvenv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=task_management

JWT_SECRET_KEY=your-long-random-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Generate a secure JWT secret

```python
import secrets

print(secrets.token_urlsafe(32))
```

Use the generated value as:

```env
JWT_SECRET_KEY=your-generated-secret
```

> Never commit `.env` to Git.

---

# 🍃 MongoDB

Make sure MongoDB is running locally or provide a MongoDB Atlas connection string.

Example:

```env
MONGODB_URL=mongodb://localhost:27017
```

The application creates the required indexes during startup.

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔐 Authentication

Authentication uses:

```text
JWT + Bearer Authentication
```

After successful login, the API returns:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

Send the token with protected requests:

```http
Authorization: Bearer <access_token>
```

Swagger UI can also be used to authorize the application.

Click:

```text
Authorize 🔓
```

and provide your JWT token.

---

# 🛣️ API Routes

## 🔐 Authentication Routes

Base URL:

```text
/auth
```

---

### `POST /auth/register`

Creates a new user account.

#### Request

```json
{
  "name": "Abhishek",
  "email": "abhi@example.com",
  "password": "password123"
}
```

#### What happens

```text
Request
   ↓
Validate UserCreate schema
   ↓
Check existing email
   ↓
Hash password using Argon2
   ↓
Create user document
   ↓
Insert into MongoDB
```

#### Response

```json
{
  "success": true,
  "message": "User Created Successfully",
  "data": {
    "id": "64...",
    "name": "Abhishek",
    "email": "abhi@example.com",
    "is_active": true,
    "is_email_verified": false
  }
}
```

---

### `POST /auth/login`

Authenticates an existing user.

#### Request

```json
{
  "email": "abhi@example.com",
  "password": "password123"
}
```

#### What happens

```text
Email
 ↓
Find user
 ↓
Verify Argon2 password
 ↓
Check account status
 ↓
Generate JWT
```

#### Response

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

---

# 👤 User Routes

Base URL:

```text
/users
```

All user routes require authentication unless explicitly configured otherwise.

---

### `GET /users/`

Returns users.

```http
GET /users/
Authorization: Bearer <token>
```

Example response:

```json
{
  "success": true,
  "message": "Users fetched successfully",
  "data": [
    {
      "id": "64...",
      "name": "Abhishek",
      "email": "abhi@example.com",
      "is_active": true,
      "is_email_verified": false
    }
  ]
}
```

---

### `GET /users/{user_id}`

Returns a specific user.

Example:

```text
GET /users/64abc123
```

The service searches MongoDB using the user's ObjectId.

If the user doesn't exist:

```text
404 USER_NOT_FOUND
```

---

### `PUT /users/{user_id}`

Updates user information.

Example:

```json
{
  "name": "Abhishek Singh",
  "email": "new@example.com"
}
```

The update uses:

```python
model_dump(exclude_unset=True)
```

so only fields provided by the client are updated.

---

### `DELETE /users/`

Deletes the currently authenticated user.

Authentication middleware identifies the user:

```python
request.state.user
```

The user's MongoDB `_id` is then used for deletion.

---

# 📝 Task Routes

Base URL:

```text
/task
```

Task routes require authentication.

Every task belongs to the authenticated user.

---

### `POST /task/`

Creates a task.

Example request:

```json
{
  "title": "Learn FastAPI",
  "description": "Learn production FastAPI architecture",
  "status": "pending",
  "priority": "medium",
  "due_date": null
}
```

The backend generates a slug from the title:

```text
Learn FastAPI
       ↓
learn-fastapi
```

The authenticated user's ID is also associated with the task.

Example MongoDB document:

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

### `GET /task/all`

Returns all non-deleted tasks belonging to the authenticated user.

The backend uses:

```python
{
    "user_id": user_id,
    "is_deleted": False
}
```

This ensures users only receive their own tasks.

If the user has no tasks, the recommended response is:

```json
{
  "success": true,
  "message": "Tasks fetched successfully",
  "data": []
}
```

---

### `GET /task/{slug}`

Returns one task using its slug.

Example:

```text
GET /task/learn-fastapi
```

The query should include the authenticated user's ID:

```python
{
    "slug": slug,
    "user_id": user_id,
    "is_deleted": False
}
```

This prevents a user from accessing another user's task.

---

### `PATCH /task/{slug}/status`

Updates the status of a task.

Example:

```json
{
  "status": "completed"
}
```

The database update should verify:

```python
{
    "slug": slug,
    "user_id": user_id,
    "is_deleted": False
}
```

Then:

```python
{
    "$set": {
        "status": "completed"
    }
}
```

This allows only the task owner to change the task.

---

### `DELETE /task/{slug}`

Soft-deletes a task.

Instead of permanently removing the MongoDB document:

```python
{
    "$set": {
        "is_deleted": True
    }
}
```

This allows the application to preserve the task record.

---

# 🧠 Task Ownership

Every task contains:

```json
{
  "user_id": "..."
}
```

When a user requests their tasks, the backend uses the authenticated user's ID:

```python
user_id = request.state.user["_id"]
```

Then:

```python
task_collection.find({
    "user_id": user_id,
    "is_deleted": False
})
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

# 🛡️ Middleware Authentication

Authentication is handled before protected routes execute.

```text
HTTP Request
     │
     ▼
Authorization Header
     │
     ▼
JWT Middleware
     │
     ├── Missing token → 401
     │
     ├── Invalid token → 401
     │
     ├── Expired token → 401
     │
     ▼
Decode JWT
     │
     ▼
Get user ID
     │
     ▼
Find user in MongoDB
     │
     ▼
request.state.user
     │
     ▼
Route
```

Protected routes can access:

```python
request.state.user
```

---

# 🔑 Password Security

Passwords are never stored as plaintext.

During registration:

```text
Plain Password
      ↓
Argon2
      ↓
Password Hash
      ↓
MongoDB
```

MongoDB stores:

```json
{
  "password_hash": "$argon2id$..."
}
```

During login:

```text
Password
   ↓
Argon2 verification
   ↓
Valid?
 ┌───┴───┐
Yes      No
 ↓        ↓
JWT      401
```

---

# 📦 Standard API Response

The project uses a common response structure:

```json
{
  "success": true,
  "message": "Operation successful",
  "data": {}
}
```

For errors:

```json
{
  "success": false,
  "message": "Task not found",
  "error": {
    "code": "TASK_NOT_FOUND"
  }
}
```

This gives the frontend a predictable API contract.

---

# ❌ Error Handling

Custom application exceptions are defined centrally.

Examples:

```text
USER_NOT_FOUND
USER_ALREADY_EXISTS
INVALID_CREDENTIALS
UNAUTHORIZED
TASK_NOT_FOUND
TASK_ALREADY_EXISTS
```

Instead of returning different error structures from every route, global exception handlers convert application exceptions into consistent HTTP responses.

---

# 🗄️ MongoDB Indexes

The application uses indexes to improve query performance and enforce uniqueness.

Examples:

```text
users.email
tasks.slug
tasks.user_id
tasks.user_id + tasks.status
```

A unique slug index prevents duplicate task slugs.

```python
await task_collection.create_index(
    [("slug", ASCENDING)],
    unique=True,
    name="unique_task_slug",
)
```

---

# 🧪 Testing

Tests can be added using:

```bash
pytest
```

Recommended test areas:

```text
tests/
├── test_auth.py
├── test_users.py
├── test_tasks.py
└── conftest.py
```

Important cases:

* User registration
* Duplicate email
* Login
* Invalid password
* Expired JWT
* Missing JWT
* Create task
* Get tasks
* Update task
* Delete task
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

Planned improvements can include:

* [ ] Refresh tokens
* [ ] Email verification
* [ ] Password reset
* [ ] Role-based authorization
* [ ] Pagination
* [ ] Task filtering
* [ ] Task sorting
* [ ] Search
* [ ] Rate limiting
* [ ] Redis caching
* [ ] Background jobs
* [ ] Automated tests
* [ ] Docker
* [ ] CI/CD
* [ ] Production logging
* [ ] API versioning

---

# 👨‍💻 Development

Run development server:

```bash
uvicorn app.main:app --reload
```

Check API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📄 License

This project is available for educational and development purposes.

---

## ⭐ Project Goal

The goal of this project is to build a clean, scalable, and production-oriented backend while learning:

```text
FastAPI
   +
MongoDB
   +
Async Programming
   +
JWT Authentication
   +
Middleware
   +
Pydantic
   +
Layered Architecture
   +
REST API Design
```

Built with ❤️ using **FastAPI + MongoDB**.
