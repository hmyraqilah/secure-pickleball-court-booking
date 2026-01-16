# Secure Pickleball Court Booking System

This is a **Django-based web application** developed for the **Secure Software Design project**. The system allows users to register, log in, and book available pickleball courts, while administrators manage courts and bookings through Django Admin. The project incorporates **OWASP secure coding practices**.

---

## Technology Used:
- Backend: Python 3.11 / Django 5.2.x
- Frontend: HTML, CSS, JavaScript
- Database: SQLite3 (default database)
- UI Styling: Bootstrap 5 (for basic UI)
  
**Packages / Libraries:**
- django-ratelimit (login rate limiting)
- python-dotenv (environment variables)

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
venv\Scripts\activate or myenv\Scripts\activate.bat


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
- Password: WAWA12345678

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
- After login process, second authentication which is the OTP code will appear in the terminal while the development server is running.
- The rate limitation for login is tested by attempting multiple logins with incorrect credentials until the error page appears.
- The session timeout is tested by leaving the session inactive for 1 minute; after that, the user cannot add a booking or view the dashboard. To continue, the user must log in again.

---

**Screenshots of System**

- Home Page
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/5ccde8e2ff62b5c2fd6ccfaff19ac8cdfdc62e49/home%20page.png)
  
- Account Registration Page
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/3529dd5b33d6dfaf077347bc4f9fadaa22c9ec68/account%20registration%20page.png)
  
- Test User Login page with OTP verification
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/3529dd5b33d6dfaf077347bc4f9fadaa22c9ec68/login%20page.png)
   ![image alt](image url)
  
- Test User Dashboard
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/3529dd5b33d6dfaf077347bc4f9fadaa22c9ec68/test%20user%20dashboard.pn)
  
- Create Booking page
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/3529dd5b33d6dfaf077347bc4f9fadaa22c9ec68/create%20booking%20page.png)
  
- Booking List page
  ![image alt](https://github.com/hmyraqilah/secure-pickleball-court-booking/blob/3529dd5b33d6dfaf077347bc4f9fadaa22c9ec68/booking%20list%20page.png)
  
- Admin verification page (RBAC verified)
  ![image alt](image url)
   
- Admin Login page
  ![image alt](image url)
  
- Admin Dashboard page
  ![image alt](image url)
  
- Admin Privilege page (add user, edit user functionality or delete user)
  ![image alt](image url) 





