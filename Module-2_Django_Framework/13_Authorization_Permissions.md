# 13. Authorization & Permissions

While **Authentication** is about verifying *who* the user is, **Authorization** is about determining *what* that user is allowed to do.

## 1. Groups & Permissions
Django includes a built-in permissions system.
- **Permissions**: Binary flags (Can view, Can add, Can change, Can delete). For every model you create, Django automatically creates these four permissions.
- **Groups**: A way of categorizing users so you can apply permissions to them en masse. For example, a "Editors" group might have permission to edit posts, but not delete them.

## 2. Restricting Access in Views
### Using Decorators (FBVs)
The `@permission_required` decorator checks if a user has a specific permission.

```python
from django.contrib.auth.decorators import permission_required

@permission_required('blog.add_post', raise_exception=True)
def create_post(request):
    # Only users with 'add_post' permission can see this
    return render(request, 'create_post.html')
```

### Checking in Logic
You can check permissions directly on the user object.
```python
if request.user.has_perm('blog.change_post'):
    # Do something
```

---

## 3. Restricting Access in Templates
You don't want a "Delete" button to appear for users who can't delete! Use the `perms` object in your templates.

```html
{% if perms.blog.delete_post %}
    <button>Delete Post</button>
{% endif %}
```

## 4. Staff vs. Superuser
- **`is_staff`**: Can log in to the Django Admin panel.
- **`is_superuser`**: Has ALL permissions without them being explicitly assigned.
- **`is_active`**: A way to "soft-delete" or deactivate a user without removing their data.

---

## 5. Row-Level Permissions (Advanced Concept)
By default, Django permissions are "All-or-Nothing" (e.g., you can edit *any* post or *no* posts). If you want a user to only edit their *own* posts, you need to add logic in your View:

```python
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    # ... rest of the logic
```

## Summary
A secure application follows the **Principle of Least Privilege**: Give users only the permissions they absolutely need to perform their job.
