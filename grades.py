"""
Système de Gestion des Notes Étudiantes
Student Grade Management System
"""


class Student:
    """Represents a student with a name and a list of grades per subject."""

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.grades: dict[str, list[float]] = {}

    def add_grade(self, subject: str, grade: float) -> None:
        """Add a grade for a given subject (0-20 scale)."""
        if not (0 <= grade <= 20):
            raise ValueError(f"Grade must be between 0 and 20, got {grade}")
        self.grades.setdefault(subject, []).append(grade)

    def average(self, subject: str | None = None) -> float:
        """Return the average grade for a subject, or the overall average."""
        if subject is not None:
            grades = self.grades.get(subject, [])
            if not grades:
                return 0.0
            return round(sum(grades) / len(grades), 2)
        all_grades = [g for gs in self.grades.values() for g in gs]
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 2)

    def mention(self) -> str:
        """Return the mention (grade label) based on overall average."""
        avg = self.average()
        if avg >= 16:
            return "Très Bien"
        if avg >= 14:
            return "Bien"
        if avg >= 12:
            return "Assez Bien"
        if avg >= 10:
            return "Passable"
        return "Insuffisant"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        student = cls(data["name"], data["student_id"])
        for subject, grades in data.get("grades", {}).items():
            for grade in grades:
                student.add_grade(subject, grade)
        return student

    def __repr__(self) -> str:
        return f"Student({self.name!r}, id={self.student_id!r}, avg={self.average()})"


class GradeBook:
    """Manages a collection of students."""

    def __init__(self):
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Add a student to the grade book."""
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id!r} already exists")
        self.students[student.student_id] = student

    def get_student(self, student_id: str) -> Student | None:
        """Retrieve a student by ID."""
        return self.students.get(student_id)

    def remove_student(self, student_id: str) -> bool:
        """Remove a student by ID. Returns True if removed, False if not found."""
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

    def class_average(self, subject: str | None = None) -> float:
        """Return the class average for a subject, or overall."""
        if not self.students:
            return 0.0
        averages = [s.average(subject) for s in self.students.values()]
        return round(sum(averages) / len(averages), 2)

    def ranking(self) -> list[Student]:
        """Return students sorted by overall average (highest first)."""
        return sorted(self.students.values(), key=lambda s: s.average(), reverse=True)

    def top_student(self) -> Student | None:
        """Return the student with the highest overall average."""
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.average())

    def to_dict(self) -> dict:
        return {sid: s.to_dict() for sid, s in self.students.items()}

    @classmethod
    def from_dict(cls, data: dict) -> "GradeBook":
        book = cls()
        for sid, student_data in data.items():
            book.add_student(Student.from_dict(student_data))
        return book
