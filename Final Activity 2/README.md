# Online Enrollment System – Student Profile View (Django)

## Features
- Student directory with search
- Click a student to open their profile
- Personal and background information
- Django admin for adding, editing, and deleting student records
- SQLite database for local development

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:
   - Windows: `py -m venv venv` then `venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create database tables: `python manage.py migrate` (the initial Student migration is included).
6. Create an admin account: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`
8. Open `http://127.0.0.1:8000/` for the student directory.
9. Open `http://127.0.0.1:8000/admin/` to manage student records.

## Add sample students
Run `python manage.py shell` and paste:

```python
from students.models import Student
Student.objects.create(
    student_id="2026-001", first_name="Juan", last_name="Dela Cruz",
    email="juan@example.com", phone="09123456789",
    birth_date="2005-04-15", gender="Male",
    address="Lopez, Quezon", guardian_name="Maria Dela Cruz",
    guardian_contact="09987654321", course="BS Information Technology",
    year_level="1st Year", section="A", previous_school="Lopez National High School"
)
Student.objects.create(
    student_id="2026-002", first_name="Maria", last_name="Santos",
    email="maria@example.com", phone="09112223334",
    birth_date="2005-08-20", gender="Female",
    address="Lopez, Quezon", guardian_name="Pedro Santos",
    guardian_contact="09998887776", course="BS Information Technology",
    year_level="1st Year", section="B", previous_school="Lopez Senior High School"
)
```

These are demonstration records. Replace them with authorized class data.

## PythonAnywhere deployment outline
1. Upload and extract this project to your PythonAnywhere account.
2. Create a virtualenv and install `requirements.txt`.
3. In the **Web** tab, create a Django web app and point its source code and working directory to this project.
4. Set the virtualenv path in the Web tab.
5. Update `ALLOWED_HOSTS` in `enrollment_system/settings.py` to include your PythonAnywhere domain.
6. Run `python manage.py migrate` in a Bash console.
7. Reload the web app from the Web tab.

Do not upload real student personal information to a public site unless you have permission and appropriate access controls. Change `SECRET_KEY`, set `DEBUG = False`, and configure static files and allowed hosts before production use.
