"""
Gestionnaire de Notes Étudiantes / Student Grade Manager
Core module for managing student grades.
"""


def calculate_average(grades):
    """Return the average of a list of grades. Returns None if the list is empty."""
    if not grades:
        return None
    return sum(grades) / len(grades)


def get_mention(average):
    """Return the French academic mention for a given average (out of 20)."""
    if average is None:
        return "Aucune note"
    if average >= 16:
        return "Très Bien"
    if average >= 14:
        return "Bien"
    if average >= 12:
        return "Assez Bien"
    if average >= 10:
        return "Passable"
    return "Insuffisant"


def add_student(students, name):
    """Add a new student with an empty grade list. Raises ValueError if already exists."""
    if name in students:
        raise ValueError(f"L'étudiant '{name}' existe déjà.")
    students[name] = []


def add_grade(students, name, grade):
    """Add a grade (0-20) for a student. Raises ValueError for invalid input."""
    if name not in students:
        raise ValueError(f"L'étudiant '{name}' n'existe pas.")
    if not (0 <= grade <= 20):
        raise ValueError("La note doit être comprise entre 0 et 20.")
    students[name].append(grade)


def get_student_report(students, name):
    """Return a report dict for a student with grades, average, and mention."""
    if name not in students:
        raise ValueError(f"L'étudiant '{name}' n'existe pas.")
    grades = students[name]
    avg = calculate_average(grades)
    return {
        "name": name,
        "grades": grades,
        "average": avg,
        "mention": get_mention(avg),
    }


def list_students(students):
    """Return a sorted list of student names."""
    return sorted(students.keys())


def get_class_ranking(students):
    """Return students sorted by average descending (best first)."""
    ranking = []
    for name, grades in students.items():
        avg = calculate_average(grades)
        ranking.append((name, avg if avg is not None else -1))
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking
