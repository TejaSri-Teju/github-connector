# 🚀 GitHub Cloud Connector (FastAPI)

## 📌 Overview

This project is a **GitHub Cloud Connector** built using FastAPI.
It integrates with GitHub APIs and allows users to perform actions like fetching repositories and managing issues.

---

## 🔐 Authentication

The application uses **GitHub Personal Access Token (PAT)** for authentication.

* Token is stored securely in a `.env` file
* It is **not hardcoded** in the source code
* Passed via `Authorization` header for all API requests

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Requests
* Pydantic

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/github-connector.git
cd github-connector
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

```bash
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env` File

Create a `.env` file in the root directory and add:

```env
GITHUB_TOKEN=your_personal_access_token
```

---

## ▶️ How to Run the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI will be available for testing APIs.

---

## 📡 API Endpoints

### 1️⃣ Fetch Repositories

* **Endpoint:** `/repos`
* **Method:** POST

**Request Body:**

```json
{
  "username": "octocat"
}
```

---

### 2️⃣ Create Issue

* **Endpoint:** `/create-issue`
* **Method:** POST

**Request Body:**

```json
{
  "owner": "your-username",
  "repo": "your-repo",
  "title": "Test Issue",
  "body": "Created via FastAPI"
}
```

---

### 3️⃣ List Issues

* **Endpoint:** `/list-issues`
* **Method:** POST

**Request Body:**

```json
{
  "owner": "your-username",
  "repo": "your-repo"
}
```

---

## ⚠️ Notes

* Ensure your GitHub token has `repo` permissions
* Do not expose `.env` file publicly
* Add `.env` to `.gitignore`

---

## ✅ Features Implemented

* GitHub API Integration
* Secure Token Handling
* REST API Endpoints
* Error Handling

---

## 🚀 Future Improvements (Optional)

* OAuth 2.0 authentication
* Async requests using `httpx`
* Docker deployment
* Logging & monitoring

---
