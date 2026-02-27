# 19. Deployment & Production

Creating a Django app is only half the battle. **Deployment** is the process of putting your code on a server so the whole world can access it.

## 1. Environment Variables
Never hardcode sensitive information in `settings.py`. Use a `.env` file and a library like `python-dotenv`.
- `SECRET_KEY`
- `DEBUG=False`
- `DATABASE_URL`

## 2. Production Settings
When you are ready to go live, update these settings:
- **`DEBUG = False`**: (Crucial!) Never run production with Debug on.
- **`ALLOWED_HOSTS`**: List the domains your site will run on (e.g., `['www.mysite.com']`).
- **`DATABASES`**: Move from SQLite to a production-grade DB like PostgreSQL or MySQL.

## 3. Static & Media Files in Production
Django's development server (`runserver`) is not designed to handle static files efficiently or securely.
1. Define `STATIC_ROOT`: The folder where all static files will be gathered.
2. Run `python manage.py collectstatic`: This copies all static files into that folder.
3. Use **WhiteNoise** (a Python library) or an external server like **Nginx** to serve these files.

## 4. Web Servers & WSGI/ASGI
A Python server like Django cannot handle millions of direct web requests. We use two layers:
1. **Application Server**: (e.g., **Gunicorn** or **Daphne**) – Runs your Python code.
2. **Reverse Proxy**: (e.g., **Nginx** or **Apache**) – Sits in front of the application server to handle high traffic, SSL (HTTPS), and security.

## 5. Deployment Options
### A. Cloud Platforms (PaaS)
- **Render / Heroku**: Very easy. They handle the server and scaling for you.
- **Railway**: Modern and developer-friendly.

### B. Virtual Private Servers (VPS)
- **DigitalOcean / AWS / Linode**: You rent a "blank" Linux server and set up everything (Nginx, Gunicorn, DB) yourself. This gives you full control.

---

## 6. The Deployment Pipeline (Automation)
For expert development, used **CI/CD** (Continuous Integration / Continuous Deployment):
1. Push code to **GitHub**.
2. GitHub Actions automatically runs your **tests**.
3. If tests pass, it automatically triggers a **deploy** to your server.

## Summary: Pro Checklist
- [ ] `DEBUG` is set to `False`.
- [ ] `SECRET_KEY` is in an environment variable.
- [ ] All database migrations are applied to the server.
- [ ] `collectstatic` has been run.
- [ ] `ALLOWED_HOSTS` is configured.
- [ ] CSRF and Session cookies are set to secure.
