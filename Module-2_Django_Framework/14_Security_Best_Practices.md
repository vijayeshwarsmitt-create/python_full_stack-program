# 14. Security Best Practices

Django was born in a newsroom environment, where speed and security are paramount. It is designed to be "Secure by Default," meaning it helps you avoid the most common web security mistakes.

## 1. Top 3 Protections in Django

### A. SQL Injection Prevention
Django’s ORM uses query parameterization. This means it separates the query logic from the data.
- **Bad (Vulnerable)**: `cursor.execute("SELECT * FROM users WHERE name = '%s'" % username)`
- **Good (Safe)**: `User.objects.filter(name=username)`

### B. Cross-Site Scripting (XSS) Protection
XSS happens when a site displays malicious JavaScript. Django templates **auto-escape** HTML.
- If a user submits `<script>alert('hacked')</script>`, Django will render it as `&lt;script&gt;...` so the browser displays it as text instead of executing it.
- *Only use the `|safe` filter if you absolutely trust the data source.*

### C. Cross-Site Request Forgery (CSRF) Protection
Ensures that a user can only submit a form that originated from your site.
- **How to use**: Always include `{% csrf_token %}` inside your `<form>`.

---

## 2. Managing the `SECRET_KEY`
The `SECRET_KEY` in `settings.py` is used for cryptographic signing (sessions, tokens).
- **CRITICAL**: Never commit your real secret key to Git. 
- Use environment variables to load it.

## 3. `DEBUG` Mode
- **Development**: `DEBUG = True` shows detailed error pages (helpful for us).
- **Production**: `DEBUG = False` is mandatory. Leaving it on exposes your file paths, variable names, and settings to hackers.

## 4. SSL / HTTPS
In production, always serve your site over HTTPS. Django has settings to help:
- `SECURE_SSL_REDIRECT = True`: Forces all traffic to HTTPS.
- `SESSION_COOKIE_SECURE = True`: Only sends session cookies over HTTPS.

## 5. Security Checklist for Deployment
1. Set `DEBUG = False`.
2. Generate a fresh, long `SECRET_KEY`.
3. Set `ALLOWED_HOSTS` to your actual domain name.
4. Ensure `DATABASES` use a strong password.
5. Run the deployment check utility:
   ```bash
   python manage.py check --deploy
   ```

## Conclusion
While Django handle most security issues automatically, security is a process, not a feature. Stay updated with the latest Django releases and always follow the official [Security Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/).
