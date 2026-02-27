# 05. Views: Function Based Views (FBV)

A **View** is the heart of your application. It contains the logic that processes a user's request and returns the appropriate response.

## 1. What is a View?
In Django, a view is simply a Python function (for FBVs) that:
1. Takes a `HttpRequest` object as its first argument.
2. Returns a `HttpResponse` object.

## 2. A Basic View
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")
```

## 3. Rendering Templates
While `HttpResponse` is useful for simple strings, you almost always want to return HTML files. For this, we use the `render()` shortcut.

```python
from django.shortcuts import render

def home_view(request):
    # Data to pass to the template
    context = {
        'title': 'Homepage',
        'message': 'Welcome to my Django site!'
    }
    return render(request, 'home.html', context)
```

## 4. Handling HTTP Methods
Views can behave differently depending on whether the user is just looking at a page (**GET**) or submitting a form (**POST**).

```python
def contact_view(request):
    if request.method == "POST":
        # Process form data
        name = request.POST.get('name')
        return HttpResponse(f"Thanks for contacting us, {name}!")
    
    # If GET, just show the form
    return render(request, 'contact.html')
```

## 5. View Shortcuts & Redirects
- **`render()`**: Combines a template with a context dictionary and returns an `HttpResponse`.
- **`redirect()`**: Sends the user to a different URL.
  ```python
  from django.shortcuts import redirect
  return redirect('home-url-name')
```
- **`get_object_or_404()`**: Tries to get an object from the database; if it doesn't exist, it automatically displays a 404 error page.
  ```python
  from django.shortcuts import get_object_or_404
  post = get_object_or_404(Post, id=pk)
  ```

---

## 6. Decorators
Decorators are used to add functionality to a view function. The most common one is `@login_required`.

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
```

## Best Practice
Keep your views "thin." Move complex business logic or data processing into your Models or separate helper functions. The View's primary job is to handle the request flow.
