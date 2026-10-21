"""Student Grade Management System (console version)."""

NUM_SUBJECTS = 7
MIN_MARK = 0
MAX_MARK = 100

# (minimum average, letter) ordered from highest to lowest
GRADE_SCALE = [
    (95, "A+"),
    (85, "A"),
    (80, "A-"),
    (75, "B+"),
    (70, "B"),
    (65, "B-"),
    (60, "C+"),
    (50, "C"),
    (40, "D"),
    (0, "F"),
]


def get_letter_grade(average):
    """Return the letter grade for an average mark."""
    for minimum, letter in GRADE_SCALE:
        if average >= minimum:
            return letter
    return "F"


def calculate_average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)


def get_student_name():
    """Ask for a name/ID until a non-empty value is entered."""
    while True:
        name = input("Enter student name or ID: ").strip()
        if name:
            return name
        print("  Name cannot be empty. Try again.")


def get_valid_mark(subject_number):
    """Ask for one mark until it is a number between MIN_MARK and MAX_MARK."""
    while True:
        raw = input(f"  Mark for subject {subject_number} ({MIN_MARK}-{MAX_MARK}): ").strip()
        try:
            mark = float(raw)
        except ValueError:
            print("  Invalid input: please enter a number.")
            continue
        if mark < MIN_MARK or mark > MAX_MARK:
            print(f"  Invalid input: mark must be between {MIN_MARK} and {MAX_MARK}.")
            continue
        return mark


def read_student():
    """Collect one student's data and return it as a dictionary."""
    name = get_student_name()
    marks = [get_valid_mark(i) for i in range(1, NUM_SUBJECTS + 1)]
    average = calculate_average(marks)
    return {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": get_letter_grade(average),
    }


def display_student(student):
    """Print one student's record."""
    marks_text = ", ".join(f"{m:g}" for m in student["marks"])
    print(f"Name:    {student['name']}")
    print(f"Marks:   {marks_text}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade:   {student['grade']}")
    print("-" * 40)


def main():
    students = []
    while True:
        students.append(read_student())
        again = input("Add another student? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n===== RESULTS =====")
    for student in students:
        display_student(student)


if __name__ == "__main__":
    main()
    