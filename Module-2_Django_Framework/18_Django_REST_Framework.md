# 18. Django REST Framework (DRF)

While standard Django is great for returning HTML templates, modern web development often requires building **APIs** (Application Programming Interfaces) that return **JSON** data for mobile apps or React/Vue frontends. **Django REST Framework (DRF)** is the industry standard for this.

## 1. Core Concepts of DRF
1. **Serializers**: Convert complex data (like Model instances) into native Python datatypes that can then be easily rendered into JSON. (Think of it as a "Form for APIs").
2. **Views**: Similar to Django views, but they return data instead of HTML.
3. **Routers**: Automatically handle URL routing for your API.

## 2. Setting Up DRF
```bash
pip install djangorestframework
```
Add `'rest_framework'` to your `INSTALLED_APPS`.

## 3. Implementation Step-by-Step

### A. Serializer
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

### B. API View
```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

### C. URL Routing
```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

---

## 4. Authentication (Token/JWT)
Unlike session-based auth (for browsers), APIs often use **Tokens**.
- **Token Auth**: A simple key sent in the header: `Authorization: Token <key>`.
- **JWT (JSON Web Tokens)**: A more advanced and scalable method.

## 5. Permissions in DRF
DRF provides granular control:
- `AllowAny`: Anyone can access.
- `IsAuthenticated`: Only logged-in users.
- `IsAdminUser`: Only staff/supers.
- `IsAuthenticatedOrReadOnly`: Anyone can look, only users can edit.

---

## Why use DRF?
- **Web-browsable API**: It generates a beautiful web interface to test your API.
- **Validation**: High-quality validation for incoming data.
- **Customizable**: You can build extremely complex API endpoints with minimal code.
