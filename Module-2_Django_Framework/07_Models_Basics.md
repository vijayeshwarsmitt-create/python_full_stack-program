# 07. Models & ORM Basics

A **Model** is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing.

## 1. What is a Model?
In Django, models are Python classes that inherit from `django.db.models.Model`. Each attribute of the class represents a database field. Django uses these classes to create the underlying database tables automatically.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
```

## 2. Common Field Types
- **`CharField`**: For small-to-medium strings. Requires `max_length`.
- **`TextField`**: For large amounts of text.
- **`IntegerField` / `FloatField` / `DecimalField`**: For numbers.
- **`BooleanField`**: True/False values.
- **`DateField` / `DateTimeField`**: For dates and times.
- **`EmailField`**: Validates that the input is a valid email.
- **`ImageField` / `FileField`**: For uploading files.

## 3. Field Options
- **`null=True`**: Django will store empty values as `NULL` in the database.
- **`blank=True`**: Allows the field to be empty in forms.
- **`default='value'`**: Sets a default value for the field.
- **`unique=True`**: Ensures every value in this table is unique.

---

## 4. Relationships (The Power of Relational DBs)
Django handles relationships between tables elegantly:
1. **Many-to-One (ForeignKey)**: A product belongs to one category, but a category has many products.
2. **Many-to-Many**: An article can have many tags, and a tag can be on many articles. 
   - `tags = models.ManyToManyField(Tag)`
3. **One-to-One**: A user has exactly one profile.
   - `user = models.OneToOneField(User, on_delete=models.CASCADE)`

---

## 5. The `__str__` Method
This is a Python method that tells Django how to display an object in the Admin panel or in shells.

```python
def __str__(self):
    return self.name
```

## 6. Meta Options
You can use a `class Meta` inside your model to define things like ordering or table names.

```python
class Meta:
    ordering = ['-created_at'] # Shows newest items first
    verbose_name_plural = "Categories"
```

## ORM: The Magic Layer
The **ORM (Object-Relational Mapper)** allows you to interact with your database using Python code instead of SQL. 
- Instead of `SELECT * FROM products;`, you write `Product.objects.all()`.
- Instead of `INSERT INTO...`, you write `Product.objects.create(...)`.
