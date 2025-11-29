# Student System – Python CLI Application

A simple modular student management system written in Python.  
The project demonstrates clean architecture, OOP principles, package structure, and basic data persistence.

---

## 🚀 Features

- Add new students (name, age, city)
- Load students from a text file
- Generate summary reports
- Modular architecture (`data`, `models`, `io`, `app`)
- JSON-like storage design (custom implementation)
- Prepared for extension (GUI, CSV export, filters, etc.)

---

## 📁 Project Structure

student_system/
│
├── app/
│ └── main.py # Entry point
│
├── data/
│ ├── database.py # Database wrapper
│ └── storage.py # Simple storage implementation
│
├── io/
│ ├── file_reader.py # Reads student data from file
│ └── report.py # Generates formatted reports
│
└── models/
└── student.py # Student model (OOP)

## ▶️ Running the application

### 1. Clone the repository

```bash
git clone https://github.com/StjepanVelc/student_system.git
cd student_system

2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install as editable package
pip install -e .

4. Run the app
python -m student_system.app.main

🛠 Technologies Used

Python 3

OOP

Custom module/package structure

CLI application design

📌 Future Improvements

GUI version (Tkinter)

CSV export

Search & filtering system

CRUD repository layer

Full desktop application

👤 Author

Stjepan Velc
Python Developer (Project-Based)
Mostar, Bosnia & Herzegovina