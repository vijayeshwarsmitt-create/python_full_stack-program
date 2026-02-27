# 21. Interview Questions

Preparing for a Django job? These are the most common questions asked in technical interviews.

---

## 🟢 Junior Level
1. **What is MVT? How is it different from MVC?**
   - *Answer*: Django uses MVT (Model-View-Template). In MVC, the Controller handles logic; in MVT, Django itself handles the "Controller" part, and the "View" handles the business logic.
2. **What are Migrations?**
   - *Answer*: Files that track changes to your Models and synchronize them with the Database schema.
3. **How do you pass data from a View to a Template?**
   - *Answer*: Using a `context` dictionary in the `render()` function.
4. **What is the purpose of `settings.py`?**
   - *Answer*: It contains the entire configuration of the Django project.

## 🟡 Intermediate Level
5. **What is an ORM? What are the benefits?**
   - *Answer*: Object-Relational Mapper. It allows developer to interact with databases using Python instead of SQL, making code more readable and database-agnostic.
6. **Explain the difference between `null=True` and `blank=True`.**
   - *Answer*: `null` is database-related (stores NULL in the DB); `blank` is validation-related (determines if a field is required in HTML forms).
7. **What is a "QuerySet" and in what sense is it "Lazy"?**
   - *Answer*: A collection of objects from the DB. It's "lazy" because it doesn't execute the SQL query until you specifically iterate over it or evaluate it.
8. **What is CSRF? How does Django prevent it?**
   - *Answer*: Cross-Site Request Forgery. Django uses a hidden token in POST forms to ensure submissions are legitimate.

## 🟣 Senior Level
9. **Explain the lifecycle of a Request in Django.**
   - *Answer*: Middleware (Request) -> URL Conf -> View -> Model/Template -> Middleware (Response) -> Client.
10. **What are signals used for? Give an example.**
    - *Answer*: For decoupling apps. Example: Automatically creating a Profile instance when a User instance is saved.
11. **When should you use Class-Based Views (CBVs) over Function-Based Views?**
    - *Answer*: For repetitive tasks like CRUD, where generic views and mixins can significantly reduce code duplication.
12. **How do you optimize database performance in Django?**
    - *Answer*: Using `select_related` (for ForeignKeys) or `prefetch_related` (for ManyToMany) to avoid the "N+1 query problem."

---

## 💡 Quick Tips for Interview Success:
- Focus on **"The Django Way"** (Batteries included, DRY).
- Be prepared to discuss **Security** (SQLi, XSS, CSRF).
- Mention **Project Experience**: Talk about the CRUD apps you've built.
