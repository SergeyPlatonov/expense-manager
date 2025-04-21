# Expense Management Application
A modern Django web application to help users track, visualize, and manage their personal spending.
## Features
- **User Authentication**: Register, login, logout, password reset/change (secure, CSRF-protected)
- **Expense Records**: Add, edit, delete, and view spending entries (title, category, amount, date, time)
- **Filtering**: View records by month or custom date range
- **Data Visualization**: Interactive dashboard with daily/category spend charts (Chart.js)
- **User Experience**: Responsive Bootstrap UI, user dropdown, modern neutral background
- **Security**: Django’s built-in authentication, session, and CSRF protection
## Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/SergeyPlatonov/expense_manager.git
cd expense_manager
```
### 2. Set up a virtual environment and install dependencies
```bash
python3 -m venv .venv

# cmd
.venv/Scripts/activate

# bash
source .venv/Scripts/activate

# PowerShell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1

pip install django
```
### 3. Create the Django project in the current directory
```
django-admin startproject expense_manager .
```
### 4. Create the main app called expenses
```
python manage.py startapp expenses
```
### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. (Optional) Create a superuser for admin access
```bash
python manage.py createsuperuser
```
### 7. Start the development server
```bash
python manage.py runserver
```
### 8. Access the app
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
### 9. Create the requirements file
```bash
pip freeze > requirements.txt
```
## Password Reset Email (Development)
To see password reset emails in your terminal, add this to your `expense_manager/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
## Project Structure
- `expense_manager/` – Django project settings and URLs
- `expenses/` – Main app (models, views, forms, templates)
- `templates/expenses/` – All HTML templates (Bootstrap, Chart.js)
## Customization & Extensibility
- Add budgeting, CSV export, or email summaries as needed
## License
Apache-2.0 license

---
**Made with Django, Bootstrap, and Chart.js**