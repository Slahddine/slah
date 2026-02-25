from student import Student


class GradeManager:
    """Manages a collection of students and their grades."""

    def __init__(self):
        self._students: dict[str, Student] = {}

    def add_student(self, name: str) -> Student:
        """Add a new student. Raises ValueError if already exists."""
        key = name.strip().lower()
        if key in self._students:
            raise ValueError(f"L'étudiant '{name}' existe déjà.")
        student = Student(name)
        self._students[key] = student
        return student

    def remove_student(self, name: str):
        """Remove a student by name. Raises KeyError if not found."""
        key = name.strip().lower()
        if key not in self._students:
            raise KeyError(f"Étudiant '{name}' introuvable.")
        del self._students[key]

    def get_student(self, name: str) -> Student:
        """Retrieve a student by name. Raises KeyError if not found."""
        key = name.strip().lower()
        if key not in self._students:
            raise KeyError(f"Étudiant '{name}' introuvable.")
        return self._students[key]

    def add_grade(self, name: str, subject: str, grade: float):
        """Add a grade for a student in a given subject."""
        student = self.get_student(name)
        student.add_grade(subject, grade)

    def all_students(self) -> list[Student]:
        """Return all students sorted by name."""
        return sorted(self._students.values(), key=lambda s: s.name.lower())

    def best_student(self) -> Student | None:
        """Return the student with the highest overall average."""
        students = self.all_students()
        if not students:
            return None
        return max(students, key=lambda s: s.average())

    def class_average(self) -> float:
        """Return the average of all students' averages."""
        students = self.all_students()
        if not students:
            return 0.0
        return round(sum(s.average() for s in students) / len(students), 2)

    def full_report(self) -> str:
        """Return a full report for all students."""
        students = self.all_students()
        if not students:
            return "Aucun étudiant enregistré."
        lines = ["=== Relevé de notes ==="]
        for student in students:
            lines.append(student.report())
            lines.append("")
        lines.append(f"Moyenne de la classe : {self.class_average()}")
        best = self.best_student()
        if best:
            lines.append(f"Meilleur étudiant : {best.name} ({best.average()}/20)")
        return "\n".join(lines)
