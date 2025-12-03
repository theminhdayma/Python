import csv
import os
import matplotlib.pyplot as plt

FILE_CSV = "Session12/data.csv"


def calculate_gpa(student):
    student["avg_score"] = round(
        (student["math_score"] + student["physics_score"] 
         + student["chemistry_score"]) / 3, 2
    )


def classify_student(student):
    gpa = student["avg_score"]
    if gpa >= 8.0:
        student["rank"] = "Excellent"
    elif gpa >= 6.5:
        student["rank"] = "Good"
    elif gpa >= 5.0:
        student["rank"] = "Average"
    else:
        student["rank"] = "Weak"


def input_score(subject_name):
    while True:
        try:
            score = float(input(f"Enter {subject_name} score (0-10): "))
            if 0 <= score <= 10:
                return score
            print("Score must be in range 0-10.")
        except ValueError:
            print("Please enter a number.")


def find_by_id(students, student_id):
    for st in students:
        if st["id"] == student_id:
            return st
    return None


def load_from_csv():
    students = []
    if not os.path.exists(FILE_CSV):
        return students
    with open(FILE_CSV, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {
                "id": row["id"],
                "name": row["name"],
                "math_score": float(row["math_score"]),
                "physics_score": float(row["physics_score"]),
                "chemistry_score": float(row["chemistry_score"]),
            }
            calculate_gpa(student)
            classify_student(student)
            students.append(student)
    return students


def save_to_csv(students):
    with open(FILE_CSV, "w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "id",
            "name",
            "math_score",
            "physics_score",
            "chemistry_score",
            "avg_score",
            "rank",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for st in students:
            writer.writerow(st)


def show_students(students):
    if not students:
        print("Student list is empty.")
        return
    print(f"{'ID':<10}{'Name':<25}{'Math':>6}{'Phys':>6}{'Chem':>6}"
          f"{'GPA':>6}{'Rank':>12}")
    print("-" * 71)
    for st in students:
        print(
            f"{st['id']:<10}{st['name']:<25}"
            f"{st['math_score']:>6.1f}{st['physics_score']:>6.1f}"
            f"{st['chemistry_score']:>6.1f}"
            f"{st['avg_score']:>6.2f}{st['rank']:>12}"
        )


def add_student(students):
    while True:
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("ID cannot be empty.")
            continue
        if find_by_id(students, student_id):
            print("ID already exists, please enter another.")
            continue
        break

    name = input("Enter name: ").strip()
    math_score = input_score("Math")
    physics_score = input_score("Physics")
    chemistry_score = input_score("Chemistry")

    student = {
        "id": student_id,
        "name": name,
        "math_score": math_score,
        "physics_score": physics_score,
        "chemistry_score": chemistry_score,
    }
    calculate_gpa(student)
    classify_student(student)
    students.append(student)
    print("Student added successfully.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    student = find_by_id(students, student_id)
    if not student:
        print("Student not found.")
        return

    print("Leave blank to keep old value.")

    s = input("New Math score: ").strip()
    if s:
        try:
            d = float(s)
            if 0 <= d <= 10:
                student["math_score"] = d
        except ValueError:
            print("Invalid Math score, keeping old value.")

    s = input("New Physics score: ").strip()
    if s:
        try:
            d = float(s)
            if 0 <= d <= 10:
                student["physics_score"] = d
        except ValueError:
            print("Invalid Physics score, keeping old value.")

    s = input("New Chemistry score: ").strip()
    if s:
        try:
            d = float(s)
            if 0 <= d <= 10:
                student["chemistry_score"] = d
        except ValueError:
            print("Invalid Chemistry score, keeping old value.")

    calculate_gpa(student)
    classify_student(student)
    print("Student updated.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_by_id(students, student_id)
    if not student:
        print("Student not found.")
        return
    confirm = input("Are you sure you want to delete? (y/n): ").lower().strip()
    if confirm == "y":
        students.remove(student)
        print("Student deleted.")
    else:
        print("Delete cancelled.")


def search_student(students):
    print("1. Search by ID")
    print("2. Search by name (approximate)")
    choice = input("Choose: ").strip()
    results = []

    if choice == "1":
        student_id = input("Enter ID: ").strip()
        st = find_by_id(students, student_id)
        if st:
            results.append(st)
    elif choice == "2":
        keyword = input("Enter name or part of name: ").strip().lower()
        results = [st for st in students if keyword in st["name"].lower()]
    else:
        print("Invalid choice.")
        return

    if not results:
        print("No student found.")
    else:
        show_students(results)


def sort_students(students):
    print("1. Sort by GPA descending")
    print("2. Sort by name A-Z")
    choice = input("Choose: ").strip()
    if choice == "1":
        students.sort(key=lambda st: st["avg_score"], reverse=True)
        print("Sorted by GPA descending.")
    elif choice == "2":
        students.sort(key=lambda st: st["name"].lower())
        print("Sorted by name A-Z.")
    else:
        print("Invalid choice.")


def statistic_by_rank(students):
    stats = {"Excellent": 0, "Good": 0, "Average": 0, "Weak": 0}
    for st in students:
        rank = st["rank"]
        if rank in stats:
            stats[rank] += 1
        else:
            stats[rank] = 1
    print("Number of students by rank:")
    for k, v in stats.items():
        print(f"- {k}: {v}")
    return stats


def draw_rank_chart(students):
    if not students:
        print("Student list is empty, cannot draw chart.")
        return
    stats = statistic_by_rank(students)
    labels = list(stats.keys())
    values = list(stats.values())

    print("1. Pie chart")
    print("2. Bar chart")
    choice = input("Choose chart type: ").strip()

    if choice == "1":
        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct="%.1f%%")
        plt.title("Student rank ratio")
    elif choice == "2":
        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=["green", "blue", "orange", "red"])
        plt.title("Number of students by rank")
        plt.xlabel("Rank")
        plt.ylabel("Count")
    else:
        print("Invalid choice.")
        return

    plt.tight_layout()
    plt.show()


def show_menu():
    students = load_from_csv()
    while True:
        print("\n====== STUDENT MANAGEMENT ======")
        print("1. Show student list")
        print("2. Add new student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Search student")
        print("6. Sort student list")
        print("7. Statistics by GPA")
        print("8. Draw rank chart")
        print("9. Save to CSV")
        print("10. Exit")
        choice = input("Choose (1-10): ").strip()

        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            sort_students(students)
        elif choice == "7":
            statistic_by_rank(students)
        elif choice == "8":
            draw_rank_chart(students)
        elif choice == "9":
            save_to_csv(students)
            print("Data saved.")
        elif choice == "10":
            save_to_csv(students)
            print("Data saved. Exit program.")
            break
        else:
            print("Invalid choice, please try again.")


show_menu()
