import json

students = {}

def load_records():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}

def save_records():
    with open("students.json", "w") as file:
        json.dump(students, file)

def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter score: "))
    students[name] = score
    print("Student added.")

def view_students():
    if not students:
        print("No records found.")
        return

    print("\n--- Student Scores ---")
    for name, score in students.items():
        print(f"{name}: {score}")

def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        score = float(input("Enter new score: "))
        students[name] = score
        print("Score updated.")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

def statistics():
    if not students:
        print("No records available.")
        return

    scores = list(students.values())
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("\n--- Statistics ---")
    print("Average Score:", average)
    print("Highest Score:", highest)
    print("Lowest Score:", lowest)

def menu():
    load_records()

    while True:
        print("\n=== STUDENT SCORE TRACKER ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Score")
        print("4. Delete Student")
        print("5. View Statistics")
        print("6. Save and Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            statistics()
        elif choice == "6":
            save_records()
            print("Records saved. Goodbye.")
            break
        else:
            print("Invalid choice.")

menu()