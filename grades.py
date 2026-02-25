"""
Système de Gestion des Notes Étudiants
Student Grade Management System
"""


class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.grades: dict[str, float] = {}

    def add_grade(self, subject: str, grade: float) -> None:
        if not (0 <= grade <= 20):
            raise ValueError(f"Grade must be between 0 and 20, got {grade}")
        self.grades[subject] = grade

    def remove_grade(self, subject: str) -> None:
        if subject not in self.grades:
            raise KeyError(f"Subject '{subject}' not found for student {self.name}")
        del self.grades[subject]

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def mention(self) -> str:
        avg = self.average()
        if avg >= 16:
            return "Très Bien"
        elif avg >= 14:
            return "Bien"
        elif avg >= 12:
            return "Assez Bien"
        elif avg >= 10:
            return "Passable"
        else:
            return "Insuffisant"

    def __repr__(self) -> str:
        return f"Student(id={self.student_id!r}, name={self.name!r}, average={self.average():.2f})"


class GradeBook:
    def __init__(self):
        self._students: dict[str, Student] = {}

    def add_student(self, student_id: str, name: str) -> Student:
        if student_id in self._students:
            raise ValueError(f"Student with ID '{student_id}' already exists")
        student = Student(student_id, name)
        self._students[student_id] = student
        return student

    def remove_student(self, student_id: str) -> None:
        if student_id not in self._students:
            raise KeyError(f"Student with ID '{student_id}' not found")
        del self._students[student_id]

    def get_student(self, student_id: str) -> Student:
        if student_id not in self._students:
            raise KeyError(f"Student with ID '{student_id}' not found")
        return self._students[student_id]

    def all_students(self) -> list[Student]:
        return list(self._students.values())

    def top_student(self) -> Student | None:
        if not self._students:
            return None
        return max(self._students.values(), key=lambda s: s.average())

    def class_average(self) -> float:
        students = self.all_students()
        if not students:
            return 0.0
        return sum(s.average() for s in students) / len(students)

    def ranking(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda s: s.average(), reverse=True)
