# 04. URL Routing & Dispatcher

URL Routing is the process of mapping a URL requested by a user to a specific Python function (View).

## 1. How the URL Dispatcher Works
When a user requests a page:
1. Django looks at the `ROOT_URLCONF` setting (usually `project_name.urls`).
2. It loads that Python module and looks for the list `urlpatterns`.
3. It runs through each URL pattern, in order, and stops at the first one that matches the requested URL.
4. It calls the associated **View** function.

## 2. Basic URL Mapping
In your `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view),
    path('about/', views.about_view),
]
```

## 3. URL Components
- **Route**: A string containing a URL pattern (e.g., `'contact/'`).
- **View**: The function to call if the pattern matches.
- **Name**: (Optional) Naming your URL lets you refer to it elsewhere in Django (templates, redirects).

## 4. Path Converters (Dynamic URLs)
Sometimes you want a URL to contain a variable, like a user ID or a post slug.
```python
urlpatterns = [
    path('user/<int:user_id>/', views.user_detail), # Matches /user/25/
    path('post/<slug:slug>/', views.post_detail),   # Matches /post/learning-django/
]
```
**Common Converters:**
- `str`: Matches any non-empty string. (Default)
- `int`: Matches zero or any positive integer.
- `slug`: Matches any slug string (letters, numbers, hyphens, underscores).
- `uuid`: Matches a formatted UUID.

## 5. Including Other URLconfs
For large projects, keeping all URLs in one file is messy. Use `include()` to link app-specific URLs.

**Project `urls.py`**:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # Delegates everything starting with /blog/ to the blog app
]
```

**App `blog/urls.py`**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),      # Matches /blog/
    path('list/', views.list),  # Matches /blog/list/
]
```

## 6. Namespace
When using `include()`, you can add a `namespace` to avoid naming conflicts between apps.
```python
path('shop/', include('shop.urls', namespace='shop')),
```
You would then refer to URLs as `'shop:index'`.
