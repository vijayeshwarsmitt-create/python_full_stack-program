# 02. Installation & Setup

Before you start building with Django, you need to set up a clean development environment.

## 1. Prerequisites
- **Python**: Ensure you have Python 3.8+ installed. 
  ```bash
  python --version
  ```

## 2. Virtual Environments (Best Practice)
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It prevents dependency conflicts between different projects.

### Step 1: Create a Virtual Environment
```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### Step 2: Activate the Environment
```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```
*You should see `(venv)` appearing at the start of your terminal prompt.*

## 3. Installing Django
With your virtual environment active, install Django using `pip`:
```bash
pip install django
```

Verify the installation:
```bash
django-admin --version
```

## 4. Creating Your First Project
A **Project** is the entire collection of settings and configurations for a particular website.

```bash
django-admin startproject my_website .
```
*(The `.` at the end tells Django to create the project in the current directory instead of creating a new folder.)*

## 5. Creating an App
In Django, a **Project** can contain multiple **Apps**. An app is a web application that does something – e.g., a blog, a database of public records, or a small poll app.

```bash
python manage.py startapp core
```

## 6. Running the Development Server
Django comes with a built-in server for development.
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. You should see the Django "Success" rocket!

---

### Summary Checklist for Every New Project:
1. `mkdir project_name`
2. `cd project_name`
3. `python -m venv venv`
4. `source venv/bin/activate`
5. `pip install django`
6. `django-admin startproject config .`
7. `python manage.py startapp main`
8. `python manage.py runserver`
