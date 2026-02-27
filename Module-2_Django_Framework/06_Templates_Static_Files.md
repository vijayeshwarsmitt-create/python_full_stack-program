# 06. Templates & Static Files

Templates and Static Files handle the "Front-end" part of your Django application.

## 1. Django Template Language (DTL)
Django allows you to inject Python-like logic into your HTML files.

### Variables
Passed from the view's context dictionary.
```html
<h1>Hello, {{ user_name }}!</h1>
```

### Tags
Used for logic like loops and conditionals.
```html
{% if is_logged_in %}
    <p>Welcome back!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

<ul>
{% for item in product_list %}
    <li>{{ item.name }}</li>
{% endfor %}
</ul>
```

---

## 2. Template Inheritance
This is one of the most powerful features of Django. It allows you to build a "base" skeleton for your site and only override specific sections in child pages.

### `base.html` (Parent)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>...</nav>

    <main>
        {% block content %}
        <!-- Child content goes here -->
        {% endblock %}
    </main>

    <footer>...</footer>
</body>
</html>
```

### `index.html` (Child)
```html
{% extends "base.html" %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h2>Welcome to the Home Page</h2>
    <p>This content is inside the base skeleton.</p>
{% endblock %}
```

---

## 3. Static Files (CSS, JS, Images)
Static files are files that don't change while the app is running.

### Setting up Static Files
1. In `settings.py`, define `STATIC_URL`.
2. Create a `static/` folder inside your app.
3. Load static in your template:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

## 4. Where does Django look for templates?
By default, Django looks for a `templates` directory inside each installed app. 
**Pro-tip**: To avoid conflicts, use a sub-directory: `app_name/templates/app_name/index.html`.

## 5. Built-in Filters
Filters modify variables before they are displayed.
- `{{ value|lower }}`: Converts to lowercase.
- `{{ value|truncatewords:20 }}`: Shows only first 20 words.
- `{{ value|default:"No description" }}`: Provides a fallback.
