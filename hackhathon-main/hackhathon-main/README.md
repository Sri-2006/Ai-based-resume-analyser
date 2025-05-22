# 💼 AI Resume Analyzer

An AI-powered resume analyzer that extracts key skills from uploaded resumes and provides a score based on predefined in-demand skills. Built with **Python**, **Flask**, and a modern **Tailwind CSS** frontend.

---

## 🚀 Features

- 📄 Upload your resume (PDF)
- 🔍 Extract skills using NLP
- 📊 Resume score based on matched skills
- 🌐 Clean, responsive UI built with Tailwind CSS
- ⚡ Lightweight and easy to deploy

---

## 📸 Screenshot

![Screenshot](https://user-images.githubusercontent.com/your-image-url.png) 

---
    
## 🛠️ Tech Stack
                  |

**Frontend**     HTML, Tailwind CSS, JavaScript Layer                          |
**Backend**     Flask                            
**AI/NLP**      OpenAI GPT-4 / spaCy / Transformers 
**Database**    PostgreSQL                       
**Hosting**     Vercel (Frontend) & Render (Backend) 

---

## 📁 Folder Structure
├── server                       # Backend (Flask)
│   ├── app.py                   # Flask application entry
│   ├── model.py                 # PostgreSQL DB functions
│   ├── parser.py                # Resume parsing logic (NLP)
│   ├── requirements.txt         # Python dependencies
│   └── venv/                    # Virtual environment (optional in .gitignore)
│
├── database/
│   └── schema.sql               # DB schema, if any (table creation)
│
    
    ── client/                      # Frontend ( HTML, Tailwind CSS, JavaScript Layer)
│   ├── public/
│   └── src/

---

**Walk through**:

# Navigate to backend
cd server

# Create a virtual environment (Windows)
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

---


👨‍💻 **Team Members**
Abhinav Aryan
Shankodeeep Chanda
Piyush Priyadarshi
Akshat Gupta


 ⚠️ This is a hackathon project. Some features may be in development.







