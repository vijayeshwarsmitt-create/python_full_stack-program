# 16. Middleware

**Middleware** is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

## 1. How Middleware Works
Imagine a series of layers that every request must pass through before it reaches your view, and every response must pass back through before it reaches the user.
- **Request Phase**: Middleware is executed from top to bottom.
- **Response Phase**: Middleware is executed from bottom to top.

## 2. Built-in Middleware
If you look at `MIDDLEWARE` in `settings.py`, you'll see several by default:
- `SecurityMiddleware`: Ensures HTTPS and other security headers.
- `SessionMiddleware`: Manages user sessions across requests.
- `AuthenticationMiddleware`: Associates users with requests using sessions.
- `CsrfViewMiddleware`: Protects against Cross-Site Request Forgery.

## 3. Creating Custom Middleware
A middleware is just a Python class with a specific structure.

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # 1. Code to be executed for each request BEFORE
        # the view (and later middleware) are called.
        print("Request is incoming!")

        response = self.get_response(request)

        # 2. Code to be executed for each request/response AFTER
        # the view is called.
        print("Response is outgoing!")

        return response
```

## 4. Registering Middleware
To activate it, add it to the `MIDDLEWARE` list in `settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ...
    'myapp.middleware.SimpleMiddleware', # Add yours here!
]
```

## 5. When to use Middleware?
- **Global logging**: Track every request made to the server.
- **IP Blocking**: Block specific users or regions.
- **Header Injection**: Add custom security headers or cookies to every response.
- **Authentication**: Custom authentication logic (e.g., Token validation).

---

## 🛑 Caution: Order Matters!
The order in `settings.py` is critical. For example, `AuthenticationMiddleware` must come *after* `SessionMiddleware` because it needs the session data to find the user.
