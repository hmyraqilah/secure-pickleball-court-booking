# Secure Pickleball Court Booking System

This is a **Django-based web application** developed for the **Secure Software Design project**. The system allows users to register, log in, and book available pickleball courts, while administrators manage courts and bookings through Django Admin. The project incorporates **OWASP secure coding practices**.

---

## Technology Used
- **Python 3.9+**  
- **Django 5.x**  
- **SQLite3** (default database)  
- **Bootstrap 5** (for basic UI styling)

---

## Project Structure
secure-pickleball-court-booking/

├── accounts/         
├── booking/           
├── core/             
├── mysecureproject/   
├── secure_booking/    
├── staticfiles/admin/  
├── templates/         
├── db.sqlite3         
├── manage.py          
├── .env               
├── security.log       
└── README.md          

---

## How to Run the Project (Windows & macOS)

### 1. Install Python
Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
> **Windows:** Tick *Add Python to PATH* during installation.

### 2. Create a Virtual Environment
**Windows :**
python -m venv venv
venv\Scripts\activate

**macOS / Linux :** 
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Development Server
Run the server with command: python manage.py runserver

Open your browser at: http://127.0.0.1:8000/ 

---
**Admin Access**

Admins manage users, groups, courts, and bookings through Django Admin: /admin/

- Username: wawa
- Password: wawa12345678

**Test User**
Test user with minimal functionality to register, login, create booking, add booking, view booking list and edit or delete booking. 

- Username: mai
- Password: 12345678

---
**Important Security Notes**

- OTP: Second-factor authentication implemented; OTP messages printed to terminal in development mode.
- Session Timeout: Users are automatically logged out after inactivity.
- Login Rate Limiting: Protects against brute-force attacks.
- Input Validation: Server-side and client-side validation implemented.
- Access Control: RBAC and object-level access control applied to prevent unauthorized actions.
- Output Encoding: Django templates escape output to prevent XSS.
- HTTPS: Considered at design level; development server uses HTTP.

---
**IMPORTANT NOTES**
- Do NOT share the venv folder.
- db.sqlite3 is included (do not delete).
- Each member must create their own virtual environment.
- Do NOT run migrations unless the database is missing.

