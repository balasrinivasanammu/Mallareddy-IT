# Student Data Management System

# A list to store the names of students
students_list = []
# A dictionary to store student data (name -> tuple of subjects and grades)
students_grades = {}
 
# A set to store the unique subjects
subjects_set = set()

def add_student(name, grades):
    """Add a new student with their grades"""
    if name not in students_list:
        students_list.append(name)
        students_grades[name] = grades
        # Add subjects to the subjects set
        for subject in grades[0]:  # Grades are stored as a tuple (subjects, marks)
            subjects_set.add(subject)
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists.")
'''
def update_grades(name, new_grades):
    """Update grades for an existing student"""
    if name in students_grades:
        students_grades[name] = new_grades
        # Update subjects set with new subjects
        for subject in new_grades[0]:
            subjects_set.add(subject)
        print(f"Grades for {name} updated successfully.")
    else:
        print(f"Student {name} not found.")

def delete_student(name):
    """Delete a student from the system"""
    if name in students_list:
        students_list.remove(name)
        del students_grades[name]
        print(f"Student {name} removed from the system.")
    else:
        print(f"Student {name} not found.")
'''
def display_all_students():
    """Display all students with their grades"""
    if students_list:
        for student in students_list:
            subjects, marks = students_grades[student]
            print(f"Student: {student}, Subjects: {subjects}, Marks: {marks}")
    else:
        print("No students found.")

def display_unique_subjects():
    """Display all unique subjects"""
    if subjects_set:
        print("Unique Subjects:", ', '.join(subjects_set))
    else:
        print("No subjects found.")

# Adding students and their grades. f calling
add_student("Alpha", (["Math", "English"], (95, 88)))
add_student("Beta", (["Math", "Science"], (80, 92)))
add_student("Gamma", (["English", "History"], (85, 79)))

# Displaying all students and their subjects
display_all_students()

# Displaying unique subjects
display_unique_subjects()

# Updating grades for a student
#update_grades("Alice", (["Math", "English", "Physics"], (98, 89, 90)))

# Displaying updated student data
#display_all_students()

# Deleting a student
#delete_student("Abi")

# Displaying all students after deletion
#display_all_students()

# Displaying unique subjects after deletion
#display_unique_subjects()


#sunnymanas@g
2311IT010182@mallareddyuniversity.ac.in
2311IT010001@mallareddyuniversity.ac.in