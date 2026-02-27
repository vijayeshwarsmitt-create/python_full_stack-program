# models.py
"""
Topic: Object-Oriented Programming (OOP)
This module defines the Student class which encapsulates student data and behaviors.
"""

class Student:
    """Represents a student in the management system."""
    
    def __init__(self, name, age, score):
        # Topic: Syntax & Variables
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        # Topic: Operators & Control Flow
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def is_passing(self):
        # Topic: Operators
        return self.score >= 60

    def to_dict(self):
        """Converts the object to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student object from a dictionary."""
        return cls(data["name"], data["age"], data["score"])
