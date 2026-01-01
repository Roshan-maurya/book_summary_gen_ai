# Book AI System (Flask + PostgreSQL + JWT + Ollama)

A Flask-based backend application that allows admin users to add books and automatically generates AI-based summaries asynchronously using a background thread.
The application uses PostgreSQL for persistence, JWT-based authentication, and role-based access control.

# Project Structer
book_ai_full/
│
├── app/
│   ├── __init__.py
│   ├── config/
│   │   └── config.py
│   │
│   ├── extensions/
│   │   └── db.py
│   │   └── jwt.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── book.py
│   │   └── review.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── book_routes.py
│   │
│   ├── services/
│   │   ├── ai_service.py
│   │   └── background_summary.py
│   │
│   └── utils/
│       └── row_required.py
│
├── create_db.py
├── run.py
├── requirements.txt
├── README.md

## Setup Steps

#### Step 1. Clone and Repository

   git clone https://github.com/Roshan-maurya/book_summary_gen_ai.git
   cd book_summary_gen_ai

#### Step 2. Download PostgreSQL and Install

   1. Create Database: CREATE DATABASE book_ai;
   2. Note your PostgreSQL credentials:

         -username
         -password
         -host
         -port
   3. Update database credentials in config.py
      Replace <db_name>,<username>,<host>,<port> and <password> with your PostgreSQL credentials.

   4. Create database table
      python create_db.py

#### Step 3. Download and Install Ollama

   -Once download in your machine. Pull mdoel. In this application, I have used llama3.2
   -If you want to use a different model, update ai_service.py:
         model = 'llama3.2'

#### step 4. Add JWT and application secret key in config.py

#### Step 5. Create Python Virtual Environment where your install project related library.

   1. python -m venv ai_env

   2. Windows
      ai_env\Scripts\activate

   3. Mac/Linux
      source ai_env/bin/activate

#### Step 6. Install Dependencies

   pip install -r requirements.txt


#### Step 7: Run the Application

   python run.py
