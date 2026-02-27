# 12. Authentication System

One of Django's "batteries" is its robust, built-in Authentication System. It handles users, groups, permissions, and cookie-based user sessions.

## 1. The Built-in User Model
By default, Django provides a `User` model with these fields:
- `username`
- `password`
- `email`
- `first_name`
- `last_name`
- `is_staff` / `is_superuser` / `is_active`

## 2. Using Authentication in Views
Django provides simple functions to handle user login and logout.

### Login
```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials")
```

### Logout
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

## 3. The `request.user` Object
In every view, you have access to `request.user`.
- If logged in, it is a `User` object.
- If not logged in, it is an `AnonymousUser` object.

```python
if request.user.is_authenticated:
    print(f"Hello, {request.user.username}")
```

## 4. Password Hashing
**Security Fact**: Django NEVER stores raw passwords in the database. It stores a "salted hash" using the PBKDF2 algorithm with a SHA256 hash. This means even if your database is hacked, the passwords remain secure.

## 5. Built-in Auth Forms
Don't write your own login forms! Django has them ready:
- `UserCreationForm`: For registration.
- `AuthenticationForm`: For login.
- `PasswordChangeForm`: For changing passwords.

---

## 6. Extending the User Model (Expert Tip)
For professional projects, it's recommended to create a **Custom User Model** at the very start.
```python
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(blank=True)
```
Then tell Django about it in `settings.py`: `AUTH_USER_MODEL = 'myapp.MyUser'`.

---

## Why use Django Auth?
- **Tested**: It’s been vetted for over 15 years.
- **Session-based**: Handles cookies and session expiration automatically.
- **Middleware**: Automatically populates `request.user` on every request.
