"""
Student Grade Management System
Système de gestion des notes étudiants
"""


class Student:
    """Represents a student with their grades."""

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.grades: dict[str, float] = {}

    def add_grade(self, subject: str, grade: float) -> None:
        """Add or update a grade for a subject."""
        if not (0 <= grade <= 20):
            raise ValueError(f"Grade must be between 0 and 20, got {grade}")
        self.grades[subject] = grade

    def average(self) -> float:
        """Calculate the student's average grade."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades.values()) / len(self.grades), 2)

    def mention(self) -> str:
        """Return the mention (letter grade) based on the average."""
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
        return f"Student(id={self.student_id!r}, name={self.name!r}, average={self.average()})"


class GradeBook:
    """Manages a collection of students and their grades."""

    def __init__(self):
        self._students: dict[str, Student] = {}

    def add_student(self, name: str, student_id: str) -> Student:
        """Add a new student to the grade book."""
        if student_id in self._students:
            raise ValueError(f"Student with ID {student_id!r} already exists")
        student = Student(name, student_id)
        self._students[student_id] = student
        return student

    def get_student(self, student_id: str) -> Student:
        """Retrieve a student by their ID."""
        if student_id not in self._students:
            raise KeyError(f"No student found with ID {student_id!r}")
        return self._students[student_id]

    def remove_student(self, student_id: str) -> None:
        """Remove a student from the grade book."""
        if student_id not in self._students:
            raise KeyError(f"No student found with ID {student_id!r}")
        del self._students[student_id]

    def all_students(self) -> list[Student]:
        """Return all students sorted by name."""
        return sorted(self._students.values(), key=lambda s: s.name)

    def top_students(self, n: int = 3) -> list[Student]:
        """Return the top n students by average grade."""
        return sorted(self._students.values(), key=lambda s: s.average(), reverse=True)[:n]

    def class_average(self) -> float:
        """Calculate the overall class average."""
        students = list(self._students.values())
        if not students:
            return 0.0
        return round(sum(s.average() for s in students) / len(students), 2)

    def subject_average(self, subject: str) -> float:
        """Calculate the average grade for a specific subject."""
        grades = [s.grades[subject] for s in self._students.values() if subject in s.grades]
        if not grades:
            return 0.0
        return round(sum(grades) / len(grades), 2)

    def report(self) -> str:
        """Generate a summary report of all students."""
        if not self._students:
            return "No students enrolled."
        lines = [
            "=" * 55,
            f"{'STUDENT REPORT':^55}",
            "=" * 55,
            f"{'ID':<10} {'Name':<20} {'Average':>7} {'Mention':<15}",
            "-" * 55,
        ]
        for student in self.all_students():
            lines.append(
                f"{student.student_id:<10} {student.name:<20} "
                f"{student.average():>7.2f} {student.mention():<15}"
            )
        lines += [
            "-" * 55,
            f"Class average: {self.class_average():.2f} / 20",
            "=" * 55,
        ]
        return "\n".join(lines)
