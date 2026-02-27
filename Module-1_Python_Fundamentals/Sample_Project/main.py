# main.py
"""
Topic: Integration & Control Flow
This is the entry point of the Student Management System.
It ties together all chapters: Syntax, Loops, Functions, Strings, Exceptions, Files, and OOP.
"""

from models import Student
from storage import save_students, load_students
from utils import calculate_average, format_student_info, display_header

def main():
    # Topic: Data Structures
    students = load_students()
    
    while True:
        # Topic: String Handling & Printing
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Class Average")
        print("4. Save & Exit")
        
        # Topic: Exception Handling & Input
        try:
            choice = input("Select an option (1-4): ")
            
            # Topic: Control Flow
            if choice == "1":
                name = input("Enter student name: ")
                # Validation loop
                while True:
                    try:
                        age = int(input("Enter student age: "))
                        score = float(input("Enter student score: "))
                        break # Break out of validation loop
                    except ValueError:
                        print("Invalid input! Please enter numbers for age and score.")
                
                # Topic: OOP (Creating Instance)
                new_student = Student(name, age, score)
                students.append(new_student)
                print(f"Student {name} added successfully!")

            elif choice == "2":
                display_header()
                if not students:
                    print("No student records found.")
                else:
                    for s in students:
                        # Topic: Function call & Formatting
                        print(format_student_info(s))
                print("-" * 80)

            elif choice == "3":
                avg = calculate_average(students)
                print(f"\nOverall Class Average Score: {avg:.2f}")

            elif choice == "4":
                save_students(students)
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice, please try again.")

        except EOFError:
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
