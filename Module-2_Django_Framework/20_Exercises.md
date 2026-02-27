# 20. Exercises

Practice is the only way to become an expert! Complete these tasks to solidify your knowledge.

---

## 🟢 LEVEL 1 - Beginners
1. **Setup**: Create a new project called `learn_django`. Create an app called `blog`. Run the server and see the success page.
2. **Views**: Create a view in `blog/views.py` that returns "Welcome to my Blog". Map it to the root URL (`/`).
3. **Templates**: Create a `base.html` with a navbar. Create an `about.html` that extends `base.html`. Use a context variable to pass the current year to the footer.

## 🟡 LEVEL 2 - Intermediate
1. **Models**: Create a `Post` model with `title`, `content`, `author`, and `created_at`.
2. **Admin**: Register it in the admin panel and customize `list_display` to show the title and date.
3. **ORM**: Open the Django shell (`python manage.py shell`) and create 5 blog posts using Python code. Then, practice filtering them by author.
4. **CRUD**: Build a view that lists all posts (`ListView`) and another that shows a single post (`DetailView`).

## 🔵 LEVEL 3 - Core Skills
1. **Forms**: Create a `PostForm`. Build a page where users can submit new blog posts.
2. **Authentication**: Restrict the "Create Post" page so that only logged-in users can access it.
3. **Authorization**: Update the "Edit Post" view so that a user can only edit posts they created.

## 🟣 LEVEL 4 - Advanced
1. **REST API**: Use DRF to create an API endpoint `/api/posts/` that returns all blog posts in JSON format.
2. **Signals**: Create a signal that logs a message to the console every time a new User is created.
3. **Middleware**: Write a simple middleware that calculates and prints the time taken to process each request.

---

## 🏆 MINI PROJECT: "Task Master"
Build a simple To-Do application that includes:
- **Models**: Task (title, description, is_completed).
- **Authentication**: Users can only see their own tasks.
- **Frontend**: A clean list view with buttons to mark tasks as complete or delete them.
- **API**: A DRF endpoint to access tasks via mobile.
