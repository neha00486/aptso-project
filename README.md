
# 🧠 APTSO — AI-Powered Recruitment & Job Management System

A full-stack job search and AI interview platform powered by **FastAPI**, **MongoDB**, **Django**, and **React**. APTSO helps candidates search live job listings, simulate interviews with AI, and offers features like resume parsing, authentication, and admin management (in progress).

# 🧠 Aptso – AI-Powered Job Search and Interview Platform

Aptso is a smart recruitment platform that helps candidates search for jobs and practice interviews with an AI interviewer. It integrates real-time job listings and simulates realistic mock interviews using voice, lip-sync, and posture detection powered by AI.
e67af417f (Add project README)

---

## 🚀 Features


### 🔍 Job Search (Frontend: HTML/CSS + Backend: FastAPI)
- Search jobs by **title** and **location**
- Live results using **Adzuna** & **JSearch** APIs
- Backend powered by FastAPI and MongoDB
- Auto-fetch jobs every 3 hours

### 🤖 AI Interview Module (Frontend: React + Backend: Django)
- Upload your resume and simulate interviews with **Google Gemini AI**
- Real-time **text-to-speech**, **lip-sync**, **microphone check**, and **non-verbal posture detection**
- Interview scoring and evaluation after completion

### 👥 User System
- Register and login (Inspired by **Indeed's** UI)
- Authenticated access to features (future expansion planned)
- Secure session handling (via Node.js backend)

### ✅ Job Search System (Frontend + FastAPI + MongoDB)
- Search jobs by **title** and **location**
- Real-time results from **Adzuna API**
- Job data stored and managed via **FastAPI** backend and **MongoDB**
- Clean, responsive frontend built with **HTML/CSS/JavaScript**

### 🤖 AI Interview System (React + Django + Google Gemini)
- Upload your **resume** (PDF/Text)
- Choose **interviewer personality**
- AI asks realistic interview questions based on resume
- Records and transcribes your answers via **microphone**
- Detects non-verbal signals like **posture and eye contact**
- Shows **lip sync animation** for responses
- Evaluates interview performance with a **score**
e67af417f (Add project README)

---

## 🛠 Tech Stack

| Frontend  | Backend      | AI & APIs     | Database |
|-----------|--------------|----------------|----------|
| HTML/CSS, JS | FastAPI, Django | Google Gemini API, Rhubarb, OpenCV | MongoDB |

---

## 🧩 Project Structure


```bash
aptso-project/
├── backend/                    # FastAPI Job Search Backend
│   ├── main.py
│   ├── database.py
│   ├── routes/
│   │   └── jobs.py
│   └── scripts/
│       ├── fetch_all_jobs.py
│       └── job_queries.py

├── frontend/                   # HTML/CSS Job Portal
│   ├── index.html
│   ├── auth.html               # Login / Signup page
│   └── style.css

├── server.js                   # Node.js login/signup backend

├── jobsearch_backend/          # MongoDB-based job search integration backend
│   └── [Optional Mongo utilities]

├── Mock_Online_InterviewAi/    # AI Interview Module
│   └── app2/
│       ├── backend/            # Django Backend
│       │   ├── views.py
│       │   ├── config.py       # GEMINI API Key goes here (not tracked)
│       │   └── manage.py
│       └── frontend/           # React Frontend
│           ├── vite + Tailwind setup
│           └── src/App.tsx, AIInterviewPage.tsx etc.

---
⚙️ Installation & Setup
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/neha00486/AI-POWERED-RECRUITMENT-JOB-MANAGEMENT-SYSTEM.git
cd AI-POWERED-RECRUITMENT-JOB-MANAGEMENT-SYSTEM
2. 🖥 Job Search Backend (FastAPI + MongoDB)
bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

3. 🌐 Frontend (HTML/CSS Job Site)
Simply open in browser:

bash
Copy
Edit
frontend/index.html
Or use Live Server in VS Code.

4. 👤 Auth System (Node.js)
bash
Copy
Edit
# From project root
npm install
node server.js
Runs on: http://localhost:3000

5. 🧠 AI Interview System (React + Django + Gemini)
Django Backend
bash
Copy
Edit
cd Mock_Online_InterviewAi/app2/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
Runs on: http://localhost:8000

React Frontend
bash
Copy
Edit
cd Mock_Online_InterviewAi/app2/frontend
npm install
npm run dev
Runs on: http://localhost:5173

Connects to Django via http://localhost:8000/api/

🔑 Configuration
Create a file: Mock_Online_InterviewAi/app2/backend/config.py

python
Copy
Edit
GEMINI_API_KEY = "your_google_gemini_api_key_here"
Add to .gitignore:

arduino
Copy
Edit
config.py
🌐 APIs Used
Adzuna API

JSearch API

Google Gemini API

📌 To-Do
✅ Job Search Integration

✅ AI Interview Simulation

✅ Resume Upload & Parsing

⏳ Admin Dashboard (Candidate + Job management)

⏳ Better Error Feedback

⏳ Deployment (e.g., Vercel + Render + MongoDB Atlas)

🤝 Contributing
Pull requests and feedback welcome! Create an issue or PR if you want to help improve APTSO.

📄 License
This project is licensed under the MIT License.

=======
aptso-project/
│
├── jobsearch_backend/ # FastAPI backend for job search
├── Mock_Online_InterviewAi/
│ └── app2/
│ ├── backend/ # Django backend for AI Interview
│ └── frontend/ # React frontend for AI Interview
├── frontend/ # HTML/CSS frontend for Aptso website
├── README.md

yaml
Copy
Edit

---

## 🔧 Setup & Installation

### 🔹 1. Clone the repository

```bash
git clone https://github.com/your-username/aptso-project.git
cd aptso-project
🔹 2. Job Search Backend (FastAPI + MongoDB)
bash
Copy
Edit
cd jobsearch_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
🔹 3. Aptso Frontend (HTML)
Use Live Server in VS Code to run:

bash
Copy
Edit
Right click index.html → Open with Live Server
🔹 4. AI Interview Backend (Django)
bash
Copy
Edit
cd Mock_Online_InterviewAi/app2/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Add your Google Gemini API key in config.py:

python
Copy
Edit
# config.py
GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY"
🔹 5. AI Interview Frontend (React)
bash
Copy
Edit
cd Mock_Online_InterviewAi/app2/frontend
npm install
npm run dev
🌐 Live Demo
If hosting on GitHub Pages or Render, you can add a link here.

👩‍💻 Developers
Neha Shaji @neha00486

Ronin-117 (AI Interview System) GitHub

📄 License
This project is for educational/demo purposes. Attribution to respective sources and APIs (Adzuna, Google Gemini, etc.).

>>>>>>> e67af417f (Add project README)
