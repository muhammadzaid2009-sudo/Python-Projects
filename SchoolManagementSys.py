# A list to store all student dictionaries
students = []

def add_student():
    print("\n--- Add New Student ---")
    roll_number = input("Enter Roll Number: ")
    
    # Check if the roll number already exists
    for student in students:
        if student["roll_number"] == roll_number:
            print("Error: A student with this Roll Number already exists!")
            return # Exit the function early if it's a duplicate
            
    name = input("Enter Student Name: ")
    father_name = input("Enter Father's Name: ")
    
    # Create a dictionary for the new student
    new_student = {
        "roll_number": roll_number,
        "name": name,
        "father_name": father_name
    }
    
    # Add to our list
    students.append(new_student)
    print("Student added successfully!")

def remove_student():
    print("\n--- Remove a Student ---")
    roll_number = input("Enter the Roll Number of the student to remove: ")
    
    # Look for the student by roll number
    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student removed successfully!")
            return # Exit the function since we found and removed them
            
    # If the loop finishes without returning, the student wasn't found
    print("Student not found with that Roll Number.")

def show_total_students():
    print("\n--- Total Students ---")
    total = len(students)
    print("Total number of students:", total)
    
    # If there are students, list them out nicely
    if total > 0:
        print("\nStudent List:")
        for student in students:
            print("Roll No:", student["roll_number"], "| Name:", student["name"], "| Father's Name:", student["father_name"])
    else:
        print("No students registered yet.")

# Main program loop
while True:
    print("\n==============================")
    print("   SCHOOL MANAGEMENT SYSTEM   ")
    print("==============================")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. See Total Students")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        show_total_students()
    elif choice == "4":
        print("Thank you for using the School Management System. Goodbye!")
        break # Breaks the loop and ends the program
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")