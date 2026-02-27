# 09. ORM Queries & CRUD Operations

The **Django ORM (Object-Relational Mapper)** allows you to perform CRUD (Create, Read, Update, Delete) operations on your database using Python objects.

## 1. Create (C)
There are two main ways to create an object:
```python
# Method 1: Instant save
product = Product.objects.create(name="Laptop", price=999.99)

# Method 2: Create instance then save
product = Product(name="Phone", price=499.00)
product.save()
```

## 2. Read (R)
This is where the ORM shines. You use **QuerySets**.
```python
# Get everything
all_products = Product.objects.all()

# Get a single object (throws error if not found or if multiple found)
product = Product.objects.get(id=1)

# Filter (Returns a QuerySet)
gaming_laptops = Product.objects.filter(category__name="Gaming")

# Exclude
non_cheap_products = Product.objects.exclude(price__lt=100)
```

### Advanced Filtering (Lookups)
- `name__icontains="laptop"`: Case-insensitive search.
- `price__gte=500`: Greater than or equal to.
- `created_at__year=2024`: Filter by year.

## 3. Update (U)
```python
# Update a single instance
product = Product.objects.get(id=1)
product.price = 899.99
product.save()

# Bulk update (More efficient)
Product.objects.filter(category="Legacy").update(active=False)
```

## 4. Delete (D)
```python
# Delete a single instance
product = Product.objects.get(id=1)
product.delete()

# Bulk delete
Product.objects.filter(active=False).delete()
```

---

## 5. Relationships in Queries
- **Follow relationship forward**: `product.category.name`
- **Follow relationship backward**: `category.product_set.all()`

## 6. Slicing & Ordering
```python
# Ordering (Alphabetical by name)
Product.objects.all().order_by('name')

# Reverse Ordering (Price high to low)
Product.objects.all().order_by('-price')

# Slicing (First 5 items - like LIMIT 5 in SQL)
Product.objects.all()[:5]
```

## 7. QuerySets are Lazy
Django doesn't actually hit the database until you iterate over the QuerySet (e.g., in a `for` loop) or print it. This allows you to chain filters together efficiently:
```python
query = Product.objects.filter(active=True)
query = query.filter(price__gt=50)
query = query.order_by('-price')
# Database is hit ONLY here:
for p in query:
    print(p.name)
```
