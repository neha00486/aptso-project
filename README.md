# AI-POWERED-RECRUITMENT-JOB-MANAGEMENT-SYSTEM

A full-stack job search platform powered by **FastAPI**, **MongoDB**, and a **responsive frontend (HTML/CSS/JS)**. This project integrates live job listings using the **Adzuna** and **JSearch** APIs and supports city-based filtering, resume parsing, and future AI interview features.

---

## 🚀 Features

* 🔍 **Job Search** by role and city (Thrissur, Kochi)
* 🌐 **Live Job Listings** using Adzuna + JSearch APIs
* 🧠 **(Coming Soon)** Resume Parsing and AI Interview Evaluation
* 🗃️ MongoDB backend for storing jobs
* 🔁 Auto-fetch jobs every 3 hours

---

## 📁 Project Structure

```
aptso-project/
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── database.py          # MongoDB connection
│   ├── scripts/
│   │   ├── fetch_all_jobs.py  # Fetch jobs from APIs
│   │   └── job_queries.py     # Search queries
├── frontend/
│   ├── index.html           # Main frontend page
│   └── style.css            # Styling
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/neha00486/AI-POWERED-RECRUITMENT-JOB-MANAGEMENT-SYSTEM.git
cd AI-POWERED-RECRUITMENT-JOB-MANAGEMENT-SYSTEM
```

### 2. Set up the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Set up the frontend

Just open `frontend/index.html` in your browser.

---

## 🌐 APIs Used

* [Adzuna API](https://developer.adzuna.com/)
* [JSearch API (RapidAPI)](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)

---

## 📌 To-Do / Upcoming

* [ ] Resume parser integration
* [ ] AI-based interview module
* [ ] User authentication system
* [ ] Admin dashboard for candidate/job management

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions or bug reports, feel free to open an issue.

---

## 📄 License

This project is licensed under the MIT License.


