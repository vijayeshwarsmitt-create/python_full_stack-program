# 01. Django Definition & MVT Architecture

## What is Django?
Django is a **high-level Python web framework** that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

### Core Philosophy
- **Batteries Included**: Django comes with almost everything you need out of the box (Admin, Auth, ORM, etc.).
- **Don't Repeat Yourself (DRY)**: Minimizes redundancy.
- **Explicit over Implicit**: A core Python principle that Django follows.

---

## The MVT Architecture
Unlike the traditional MVC (Model-View-Controller) pattern, Django uses a slightly modified pattern called **MVT (Model-View-Template)**.

### 1. Model (Data Layer)
- **Role**: Handles everything to do with data.
- **Description**: It is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
- **Tech**: Django ORM (Object-Relational Mapper).

### 2. View (Business Logic Layer)
- **Role**: The "bridge" between the Model and the Template.
- **Description**: A view is a Python function (or class-based view) that receives a web request and returns a web response. It fetches data from the Model and passes it to a Template.

### 3. Template (Presentation Layer)
- **Role**: Handles how the data is displayed.
- **Description**: A template is a text file (like HTML) that defines the structure or layout of the final response. It uses **Django Template Language (DTL)** to inject data passed from the View.

### How they work together:
1. **User** requests a URL (e.g., `/profile/`).
2. **URL Dispatcher** finds the matching **View**.
3. The **View** talks to the **Model** to get user data.
4. The **Model** returns data from the Database.
5. The **View** passes this data to the **Template**.
6. The **Template** renders HTML and sends it back to the **View**.
7. The **View** sends the final **HTML Response** to the User's browser.

---

## Why Choose Django?
1. **Highly Secure**: Protections against SQL Injection, XSS, CSRF, and clickjacking are built-in.
2. **Scalable**: Used by traffic-heavy sites like Instagram, Spotify, and YouTube.
3. **Versatile**: Used for CMSs, social networks, scientific computing platforms, and more.
4. **ORM**: You don't need to write SQL for basic database operations.
5. **Admin Interface**: A professional, ready-to-use administration dashboard is automatically generated for your models.
