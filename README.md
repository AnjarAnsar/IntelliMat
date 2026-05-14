# AI-Based Material Selection & Recommendation System

An intelligent material recommendation system that predicts material performance and suggests the most suitable materials based on user requirements.

The project uses:

- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** FastAPI + Machine Learning
- **ML Libraries:** Scikit-learn, Pandas, NumPy

---

# Project Structure

```bash
material-selection-project/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   ├── pipelines/
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# Features

- Predicts:
  - Wear Rate
  - Friction Coefficient

- Recommends best matching materials
- Machine Learning powered predictions
- Interactive frontend UI
- FastAPI backend integration
- Real-time recommendation workflow

---

# Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd material-selection-project
```

---

# Backend Setup

Move to backend directory:

```bash
cd backend
```

## Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend Server

```bash
uvicorn app:app --reload
```

Backend will run at:

```bash
http://localhost:8000
```

---

# Frontend Setup

Open another terminal.

Move to frontend directory:

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Run Frontend

```bash
npm run dev
```

Frontend will run at:

```bash
http://localhost:5173
```

---

# Tech Stack

## Frontend
- React
- Vite
- Tailwind CSS
- DaisyUI

## Backend
- FastAPI
- Python

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

---

# API Workflow

1. User enters input parameters from frontend
2. Frontend sends request to FastAPI backend
3. ML models predict:
   - Wear Rate
   - Friction Coefficient
4. Recommendation pipeline suggests best materials
5. Results displayed on frontend

---

# Future Improvements

- AutoML integration
- ChatGPT-like prompt interface
- Authentication system
- Database integration
- Deployment on cloud platforms
- Advanced visualization dashboard

---

# Author

Developed as an AI-powered engineering material recommendation project.
