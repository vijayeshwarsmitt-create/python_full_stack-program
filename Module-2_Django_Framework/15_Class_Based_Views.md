# 15. Class-Based Views (CBV)

As your application grows, using Function-Based Views (FBVs) can lead to a lot of repetitive code. **Class-Based Views (CBVs)** solve this by allowing you to use inheritance and reusable patterns.

## 1. Why use CBVs?
1. **DRY (Don't Repeat Yourself)**: You can reuse common logic.
2. **Organization**: Separate code by HTTP method (`get()`, `post()`) instead of using `if request.method == "POST"`.
3. **Built-in Mixins**: Quickly add features like login requirements.

## 2. Basic Generic Views
Django provides several "Generic" views that handle common tasks out of the box.

### `ListView` (Displaying a list of items)
```python
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html' # Default: student_list.html
    context_object_name = 'students'     # Default: object_list
    paginate_by = 10                     # Adds pagination automatically!
```

### `DetailView` (Displaying one specific item)
```python
from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    # Automatically expects a 'pk' or 'slug' in the URL
```

### `CreateView` / `UpdateView` / `DeleteView` (CRUD)
```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age', 'score']
    success_url = reverse_lazy('student-list')
```

---

## 3. URLs for CBVs
Since CBVs are classes, you must call the `.as_view()` method in your `urls.py`.

```python
path('students/', StudentListView.as_view(), name='student-list'),
path('student/add/', StudentCreateView.as_view(), name='student-add'),
```

---

## 4. Customizing CBVs
You can override specific methods to add your own logic.
- **`get_queryset()`**: To filter the items shown.
- **`get_context_data()`**: To add extra variables to the template.
- **`form_valid()`**: To perform actions after a successful form submission (like setting the user).

```python
class MyListView(ListView):
    def get_queryset(self):
        # Only show students with score > 80
        return Student.objects.filter(score__gt=80)
```

## 5. Mixins (Multi-inheritance)
Mixins are like plugins for classes.
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class SecretListView(LoginRequiredMixin, ListView):
    # Only logged-in users can access this class
    model = Student
```

## Summary: FBV vs. CBV
- **FBVs** are simple and easy to read. Best for unique, custom logic.
- **CBVs** are powerful and efficient. Best for standard CRUD operations and large, complex projects.
