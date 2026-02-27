# 03. Understanding Project Structure

When you create a Django project and app, several files and directories are automatically generated. Understanding what each one does is crucial for building organized applications.

## 1. Project Directory (`my_website/`)
This is the root folder of your project.

### `manage.py`
- **What it is**: A command-line utility that lets you interact with this Django project.
- **Role**: You use it to run the server, create apps, work with migrations, and more. 
- **Example**: `python manage.py runserver`

### The Inner Project Folder (`my_website/`)
This is the actual Python package for your project.
- #### `__init__.py`
  - An empty file that tells Python this directory should be considered a Python package.
- #### `settings.py`
  - **The Brain of your project**: Contains all configurations (Database settings, Middleware, Installed Apps, Security keys, Time zones, etc.).
- #### `urls.py`
  - **The Router**: The "table of contents" for your website. It maps URL patterns to views.
- #### `asgi.py` & `wsgi.py`
  - Entry points for web servers to serve your project (ASGI for asynchronous, WSGI for synchronous).

---

## 2. App Directory (`core/`)
An app is a submodule that handles specific functionality (e.g., users, blog, products).

- #### `migrations/`
  - Stores database migration files (tracking changes to your data models).
- #### `admin.py`
  - Where you register your models so they show up in the Django Admin panel.
- #### `apps.py`
  - Contains configuration for the app itself.
- #### `models.py`
  - **Crucial**: Where you define your database tables as Python classes.
- #### `tests.py`
  - Where you write automated tests for your app.
- #### `views.py`
  - **Crucial**: Where the logic happens. It handles requests and returns responses.

---

## The "Project vs App" Concept
- **Project**: The whole website/container. It contains configuration and multiple apps.
- **App**: A web application that does one specific thing. 
- **Analogy**: A Project is like a Mobile Phone; an App is like the Camera or WhatsApp installed on it.

## Best Practice: Modular Design
Don't put everything in one app! If your website has a store and a forum, make `shop` and `forum` separate apps. This makes your code reusable and easier to maintain.
