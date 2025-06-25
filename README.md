

# APTSO - AI-Powered Recruitment Platform

Aptso is an intelligent job search and interview platform. It combines:

* 🔎 **Job Search** using FastAPI, MongoDB, and real-time job APIs (like Adzuna).
* 🧠 **AI Interview** powered by Google Gemini API, using a 3D React UI and Django backend.

---

## 🌐 Live Features

* Search for jobs by title and location.
* AI-powered 3D interview simulation (Gemini + Lip Sync + Webcam).
* Resume upload and evaluation.
* User sign-up/login with authentication.

---

## 📁 Project Structure

```
aptso-project/
│
├── jobsearch_backend/        # FastAPI + MongoDB backend for job search
├── frontend/                 # HTML/CSS-based job search UI
├── Mock_Online_InterviewAi/ # AI Interview (React + Django)
│   └── app2/
│       ├── backend/          # Django backend
│       └── frontend/         # React + Vite frontend
```

---

## 1. ⚙ Job Search Backend (FastAPI + MongoDB)

### Setup

```bash
cd jobsearch_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Make sure MongoDB is running locally or update `database.py` with your Mongo URI.

---

## 2. 🧠 AI Interview System (React + Django)

### Backend (Django)

```bash
cd Mock_Online_InterviewAi/app2/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Make sure to add your **Gemini API Key** in `config.py`:

```python
# backend/config.py
GEMINI_API_KEY = "your_actual_api_key"
```

### Frontend (React + Vite)

```bash
cd Mock_Online_InterviewAi/app2/frontend
npm install
npm run dev
```

Runs on: [http://localhost:3000](http://localhost:3000)

---

## 3. 🌍 Main Aptso Job Search UI (HTML/CSS)

Open with Live Server or directly:

```bash
cd frontend
Open index.html with Live Server (or use localhost:5500)
```

Make sure `<form>` in `index.html` sends job search requests to:

```js
fetch('http://localhost:8000/search', {
```

---

## 🔑 Authentication (Login/Signup)

* The frontend UI uses `auth.html` and `auth.js`.
* Backend API: `server.js` handles registration, login, logout, and JWT sessions.
* Run it from the root or `auth_backend` (if separated):

```bash
node server.js
```

---

## ✅ Run All Servers (Recommended in Separate Terminals)

1. `jobsearch_backend` → FastAPI
2. `Mock_Online_InterviewAi/app2/backend` → Django
3. `Mock_Online_InterviewAi/app2/frontend` → React
4. `frontend/index.html` → Open with Live Server

---

## 📄 License

MIT License – use it freely for educational or commercial purposes.


