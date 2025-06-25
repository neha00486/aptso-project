# 🧠 APTSO — AI-Powered Recruitment & Job Management System

A full-stack job search and AI interview platform powered by **FastAPI**, **MongoDB**, **Django**, and **React**. APTSO helps candidates search live job listings, simulate interviews with AI, and offers features like resume parsing, authentication, and admin management (in progress).

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

---

## 📁 Project Structure

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

