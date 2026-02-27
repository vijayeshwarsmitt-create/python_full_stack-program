# utils.py
"""
Topic: Functions, String Handling, and Calculations
This module provides utility functions for data processing and formatting.
"""

def calculate_average(students):
    """Calculates the average score of a list of students."""
    # Topic: Control Flow & Operators
    if not students:
        return 0.0
    
    total = sum(s.score for s in students)
    return total / len(students)

def format_student_info(student):
    """Returns a formatted string representing student information."""
    # Topic: String Handling (f-strings)
    status = "PASS" if student.is_passing() else "FAIL"
    return f"Name: {student.name:<15} | Age: {student.age:<3} | Score: {student.score:<5} | Grade: {student.get_grade():<2} | Status: {status}"

def display_header():
    """Prints a styled header for the report."""
    # Topic: String Handling (multiplication)
    print("\n" + "="*80)
    print(f"{'STUDENT MANAGEMENT SYSTEM REPORT':^80}")
    print("="*80)
