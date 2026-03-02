'''Student Marks Analysis System
Features:
- Average Marks
- Highest Marks
- Lowest Marks
- Sort Students by Marks
- Top 3 Students
- Grading System
- Add New Student
'''

def create_dict():
    students = {}
    n = int(input('Enter the number of students:'))
    i = 0
    while i < n:
        name = input('Enter the name of student:')
        marks = int(input('Enter the marks of student:'))
        students[name] = marks
        i += 1
    return students

def average_marks(students):
    total_marks = sum(students.values())
    average = total_marks/len(students)
    return average

def highest_marks(students):
    highest_student = max(students, key = students.get)
    highest = students[highest_student]
    return f'{highest_student} --> {highest}'

def lowest_marks(students):
    lowest_student = min(students, key = students.get)
    lowest = students[lowest_student]
    return f'{lowest_student} --> {lowest}'

def sort_students(students):
    sorted_list = sorted(students.items(), key = lambda x : x[1], reverse = True)
    return sorted_list

def top3_students(students):
    top3 = sorted(students.items(), key = lambda x : x[1], reverse = True)[:3]
    return top3

def grade_system(students):
    grade = {}
    for name, mark in students.items():
        if mark >= 90:
            grade[name] = 'A'
        elif mark >= 75:
            grade[name] = 'B'
        elif mark >= 60:
            grade[name] = 'C'
        elif mark >= 50:
            grade[name] = 'D'
        else:
            grade[name] = 'F'
    return grade

def add_new_student(students):
    name = input('Enter the name of student:')
    marks = int(input('Enter the marks of student:'))
    students[name] = marks

students = create_dict()

while True:
    print('----Student Marks Analysis----')
    print('1. Show Average Marks')
    print('2. Show Highest Marks')
    print('3. Show Lowest Marks')
    print('4. Sort Students by Marks')
    print('5. Show Top 3 Students')
    print('6. Show Grade System')
    print('7. Add New Student')
    print('8. Exit')

    choice = int(input('Enter your choice:'))
    if choice == 1:
        print('Average Marks:', average_marks(students))
    elif choice == 2:
        print('Highest Marks:', highest_marks(students))
    elif choice == 3:
        print('Lowest Marks:', lowest_marks(students))
    elif choice == 4:
        print('Sorted Students by Marks:', sort_students(students))
    elif choice == 5:
        print('Top 3 Students:', top3_students(students))
    elif choice == 6:
        print('Grading System:', grade_system(students))
    elif choice == 7:
        add_new_student(students)
    elif choice == 8:
        print('Exiting...')
        break
    else:
        print('Invalid choice')






