# 17. Signals

**Signals** allow decoupled applications to get notified when actions occur elsewhere in the framework. Essentially, signals allow some "senders" to notify a set of "receivers" that some action has taken place.

## 1. The Concept
Think of it as an **Observer Pattern**. Instead of putting logic for three different tasks into one function, you can "broadcast" an event and let other parts of the system react to it.

## 2. Common Built-in Signals
- `post_save`: Sent after a model is saved. (Most common)
- `pre_save`: Sent before a model is saved.
- `post_delete`: Sent after a model is deleted.
- `user_logged_in`: Sent when a user logs in.

## 3. Implementing a Signal
A typical use case is creating a "Profile" object automatically every time a new "User" is created.

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

## 4. Where to define Signals?
- **Receiver functions**: Put them in a file called `signals.py` inside your app.
- **Registration**: You must tell Django to load this file. Do this in your app's `apps.py`:

```python
# apps.py
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals # Important: Load the signals!
```

---

## 5. Pros and Cons
### Pros:
- **Decoupling**: Keeps code clean; the User model doesn't need to know about the Profile model.
- **Maintainability**: You can add/remove reactions without touching the core logic.

### Cons:
- **Hidden Logic**: It can be hard to track what's happening if you have too many signals.
- **Performance**: Chaining too many signals can slow down database operations.

## Summary
Signals are an expert-level tool for building complex, reactive systems. Use them sparingly and keep them organized!
