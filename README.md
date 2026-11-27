# Employee Management & Payslip Generation System

## Project Overview

The Employee Management and Payslip Generation System is a web-based application developed using Python Flask and SQLite.

The application helps manage employee information, calculate monthly salaries based on employee details and leave days, and generate payslip information.

This project was developed as a personal project to practise Python web development, database integration, and backend application development.

## Features

- **Employee Management:** Add, view, update, and delete employee records.
- **Salary Calculation:** Calculate employee salaries based on basic salary, leave days, and applicable allowances and deductions.
- **Payslip Generation:** Retrieve payslip details using employee ID and salary month.
- **Database Integration:** Store and retrieve employee and salary information using SQLite.
- **Web Interface:** Use HTML templates to interact with the application.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git
- GitHub

## Project Structure

```text
Payslip-System/
│
├── app.py
├── db_employee.db
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│
└── templates/
    ├── index.html
    ├── employee.html
    ├── edit.html
    ├── salary.html
    └── payslip.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ThafsiHassan/Payslip-System.git
```

### 2. Navigate to the project directory

```bash
cd Payslip-System
```

### 3. Create a virtual environment

```bash
python -m venv myvenv
```

### 4. Activate the virtual environment

For Windows:

```bash
myvenv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

**Note:** The application requires a properly initialized SQLite database. Use only sample employee data when testing.

## Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using Python Flask.
- Implementing CRUD operations.
- Connecting Python applications with SQLite databases.
- Working with HTML templates.
- Implementing basic salary calculation logic.
- Using Git and GitHub for version control.

## Future Improvements

- Implement user authentication and authorization.
- Improve input validation and error handling.
- Add PDF payslip downloads.
- Improve the user interface.
- Deploy the application online.

## Author

**Thafseena Hassan**

GitHub: https://github.com/ThafsiHassan
