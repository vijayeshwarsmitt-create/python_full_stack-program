# 11. Forms & ModelForms

Handling HTML forms is one of the most complex tasks in web development. Django's Form system simplifies this by automating data validation, security (CSRF), and HTML generation.

## 1. Django Forms vs ModelForms
- **`forms.Form`**: Used when the form data isn't directly related to a database model (e.g., a contact form).
- **`forms.ModelForm`**: Used when the form is designed to create or update a database object. This is what you'll use 90% of the time.

## 2. Creating a ModelForm
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'score'] # Or '__all__'
        
        # Adding CSS classes for styling (e.g., Bootstrap)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
```

## 3. Using the Form in a View
This pattern is a foundational building block of Django.

```python
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST) # Bind data to form
        if form.is_valid():
            form.save() # Saves to database!
            return redirect('success_url')
    else:
        form = StudentForm() # An empty form
        
    return render(request, 'add_student.html', {'form': form})
```

## 4. Rendering in Templates
Django provides several helpers to display forms.
```html
<form method="POST">
    {% csrf_token %} <!-- SECURITY: Never forget this! -->
    
    {{ form.as_p }} <!-- Renders fields inside <p> tags -->
    
    <button type="submit">Submit</button>
</form>
```
Other options: `{{ form.as_table }}`, `{{ form.as_ul }}`.

## 5. Security: CSRF (Cross-Site Request Forgery)
Django forces you to include a `{% csrf_token %}` in every `POST` form. This ensures that the form submission is coming from your own website and not a malicious third-party site.

## 6. Custom Validation
You can add your own rules inside the form class.

```python
def clean_score(self):
    score = self.cleaned_data.get('score')
    if score < 0 or score > 100:
        raise forms.ValidationError("Score must be between 0 and 100.")
    return score
```

---

## 7. CRUD App Summary
By combining **Models + Views + Forms**, you can build a complete CRUD application:
1. **Create**: User submits a `ModelForm`.
2. **Read**: `Model.objects.all()` shown in a template.
3. **Update**: `ModelForm(instance=obj)` loaded with existing data.
4. **Delete**: `obj.delete()` triggered by a button.
