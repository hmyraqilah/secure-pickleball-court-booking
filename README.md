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
├── accounts/          # User authentication (login, logout, registration)
├── booking/           # Booking management (create, view bookings)
├── core/              # Core settings and main URLs
├── mysecureproject/   # Project settings
├── secure_booking/    # Main app for court management and bookings
├── staticfiles/admin/ # Admin static files
├── templates/         # HTML templates (base, auth, booking)
├── db.sqlite3         # Database (included)
├── manage.py          # Django management commands
├── .env               # Environment variables (do NOT share)
├── security.log       # Security logs
└── README.md          # Project documentation


