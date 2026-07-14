# 🚀 Task API

A simple **CRUD (Create, Read, Update, Delete) REST API** built using **FastAPI**. This project demonstrates the fundamentals of RESTful API development, request validation, error handling, and automatic API documentation using Swagger UI.

---

## 📌 Project Overview

Task API is an in-memory task management application that allows users to:

* Create tasks
* Retrieve all tasks
* Retrieve a task by ID
* Update existing tasks
* Delete tasks

This project is built without a database. All data is stored temporarily in memory while the application is running.

---

## ✨ Features

* RESTful CRUD APIs
* FastAPI framework
* Automatic Swagger UI documentation
* Request validation using Pydantic
* Proper HTTP status codes
* Error handling
* In-memory data storage
* Clean and modular code

---

## 🛠️ Technologies Used

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

# 📂 Project Structure

```text
task-api/
│
├── screenshots/
│   ├── 01-swagger-home.png
│   ├── 02-get-all-tasks.png
│   ├── 03-get-task-by-id.png
│   ├── 04-create-task.png
│   ├── 05-update-task.png
│   ├── 06-delete-task.png
│   ├── 07-health-endpoint.png
│   └── 08-project-structure.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/task-api.git
```

### Navigate into the project

```bash
cd task-api
```

### Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

OpenAPI JSON

```text
http://127.0.0.1:8000/openapi.json
```

---

# 📌 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/`           | API information         |
| GET    | `/health`     | Health check            |
| GET    | `/tasks`      | Get all tasks           |
| GET    | `/tasks/{id}` | Get task by ID          |
| POST   | `/tasks`      | Create a new task       |
| PUT    | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task           |

---

# 🧪 Sample Requests

## Create Task

**POST** `/tasks`

```json
{
  "title": "Buy Milk"
}
```

Response

```json
{
  "id": 4,
  "title": "Buy Milk",
  "done": false
}
```

---

## Get All Tasks

**GET** `/tasks`

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Complete Assignment",
    "done": false
  }
]
```

---

## Update Task

**PUT** `/tasks/1`

```json
{
  "title": "Learn FastAPI Basics",
  "done": true
}
```

---

## Delete Task

**DELETE** `/tasks/1`

Returns:

```text
204 No Content
```

---

# 📷 Screenshots

## Swagger UI

```
screenshots/01-swagger-home.png
```

## Get All Tasks

```
screenshots/02-get-all-tasks.png
```

## Get Task By ID

```
screenshots/03-get-task-by-id.png
```

## Create Task

```
screenshots/04-create-task.png
```

## Update Task

```
screenshots/05-update-task.png
```

## Delete Task

```
screenshots/06-delete-task.png
```

## Health Endpoint

```
screenshots/07-health-endpoint.png
```

---

# ✅ HTTP Status Codes

| Status Code | Meaning     |
| ----------- | ----------- |
| 200         | OK          |
| 201         | Created     |
| 204         | No Content  |
| 400         | Bad Request |
| 404         | Not Found   |

---

# 🚀 Future Improvements

* SQLite/MySQL integration
* User authentication
* JWT authorization
* Persistent database storage
* Pagination
* Search functionality
* Unit testing
* Docker support
* Deployment on Render or Railway

---

# 👩‍💻 Author

**Puru Ruchitha**

B.Tech Computer Science & Engineering

Built using **FastAPI** and **Python**.
