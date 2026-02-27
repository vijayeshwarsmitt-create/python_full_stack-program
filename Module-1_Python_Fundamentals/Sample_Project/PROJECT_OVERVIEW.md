# Project Overview: Student Management System

This project is designed to demonstrate every core concept covered in **Module-1: Python Fundamentals**. Below is a mapping of each topic to its implementation within the project.

## Topic Mapping

### 1. Syntax & Variables
- **Where:** `models.py` (Line 11-13)
- **Detail:** Defining attributes like `self.name`, `self.age`, and `self.score` using appropriate data types (String, Integer, Float).

### 2. Operators & Control Flow
- **Where:** `models.py` (Line 16-25), `main.py` (Line 23-60)
- **Detail:** 
    - Logical operators in `get_grade()` to determine a student's letter grade.
    - `while True` loop in `main.py` for the menu and input validation.
    - `if-elif-else` blocks for menu selection.

### 3. Functions & Modules
- **Where:** Throughout all files (`main.py`, `models.py`, `storage.py`, `utils.py`).
- **Detail:** Breaking code into logical, reusable functions and organizing them into separate modules for better maintainability.

### 4. Data Structures
- **Where:** `main.py` (Line 13), `storage.py` (Line 14)
- **Detail:** Storing student objects in a **List**. Using **List Comprehensions** for efficient data conversion in `save_students`.

### 5. String Handling
- **Where:** `utils.py` (Line 20-22), `main.py` (Line 17-21)
- **Detail:** 
    - Using **f-strings** for alignment and padding in reports.
    - Using string multiplication (`"="*80`) for visual separators.

### 6. Exception Handling
- **Where:** `main.py` (Line 29-36), `storage.py` (Line 19-21)
- **Detail:** 
    - Using `try-except` blocks to handle `ValueError` during user input.
    - Handling `IOError` and `JSONDecodeError` during file operations.

### 7. File Handling
- **Where:** `storage.py`
- **Detail:** Using the `json` module to persist and retrieve student data from a local file (`students.json`).

### 8. Object-Oriented Programming (OOP)
- **Where:** `models.py`
- **Detail:** Defining a `Student` **Class** with an `__init__` constructor and instance methods to encapsulate behavior.

---

## How to Run the Project

1. Navigate to the project folder:
   ```bash
   cd Module-1_Python_Fundamentals/Sample_Project/
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the CLI prompts to manage student data.
