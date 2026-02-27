# storage.py
"""
Topic: File Handling & Exception Handling
This module handles persistence of student data using JSON.
"""

import json
from pathlib import Path

STORAGE_FILE = Path(__file__).parent / "students.json"

def save_students(students_list):
    """Saves a list of student objects to a JSON file."""
    # Topic: Data Structures (List Comprehension)
    data = [s.to_dict() for s in students_list]
    
    # Topic: File Handling
    try:
        with open(STORAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {STORAGE_FILE.name}")
    except IOError as e:
        # Topic: Exception Handling
        print(f"Error saving data: {e}")

def load_students():
    """Loads students from a JSON file and returns a list of Student objects."""
    if not STORAGE_FILE.exists():
        return []

    try:
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
            # Importing Student here to avoid circular dependency
            from models import Student
            return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading data: {e}")
        return []
