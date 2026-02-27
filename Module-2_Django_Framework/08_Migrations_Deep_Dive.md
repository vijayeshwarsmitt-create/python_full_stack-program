# 08. Migrations: Deep Dive

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They are designed to be mostly automatic.

## 1. The Migration Workflow
Whenever you change `models.py`, follow these three steps:
1. **Change the Model**: Edit your Python class in `models.py`.
2. **Create Migrations**: Run `python manage.py makemigrations`. This creates a new file in the `migrations/` folder.
3. **Apply Migrations**: Run `python manage.py migrate`. This actually updates the database tables.

---

## 2. Core Commands
- **`makemigrations`**: Scans your `models.py` files for changes and creates new migration files.
- **`migrate`**: Synchronizes the database state with the current set of models and migrations. It tracks which migrations have been run in a table called `django_migrations`.
- **`showmigrations`**: Lists all migrations in the project and shows whether they have been applied (`[X]`) or not (`[ ]`).
- **`sqlmigrate <app_name> <migration_number>`**: Shows the raw SQL that Django will execute for a specific migration. (Great for debugging or DBAs!)

---

## 3. Why are Migrations Important?
- **Version Control for your Database**: Migrations are files that can be committed to Git. This allows your teammates to have the exact same database structure as you.
- **Database Agnostic**: You can write your models once, and migrations will handle the SQL differences whether you use SQLite, PostgreSQL, or MySQL.
- **Rollbacks**: You can revert to a previous state by migrating to an earlier number: `python manage.py migrate my_app 0001`.

---

## 4. Handling Contentious Changes
### Adding a non-nullable field:
If you have data in your database and try to add a new field without a default value, Django will ask you:
1. "Provide a one-off default now."
2. "Quit, and let me add a default in `models.py`."
*Always choose a default or set `null=True` to avoid errors.*

### Renaming a field:
Django is smart. If you rename a field, `makemigrations` will ask: "Did you rename product.title to product.name?". Answer 'y' and it will generate a `RenameField` operation instead of deleting and recreating the column (which would lose data!).

---

## 5. Good Migration Habits
- **Commit migraton files**: Never `gitignore` your `migrations/` folder.
- **Don't delete migration files**: Unless you are "squashing" them, keep them to maintain history.
- **Don't edit migration files manually**: Unless you are an expert performing a data migration or complex schema change.
