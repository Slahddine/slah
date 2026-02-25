"""
Système de Gestion des Notes Étudiants
Student Grade Management System
"""


class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.grades: dict[str, float] = {}

    def add_grade(self, subject: str, grade: float) -> None:
        if not (0 <= grade <= 20):
            raise ValueError(f"Grade must be between 0 and 20, got {grade}")
        self.grades[subject] = grade

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

    def is_passing(self) -> bool:
        return self.average() >= 10.0

    def report(self) -> str:
        lines = [
            f"Étudiant : {self.name} (ID: {self.student_id})",
            "-" * 40,
        ]
        for subject, grade in self.grades.items():
            lines.append(f"  {subject:<20} : {grade:.2f}/20")
        lines.append("-" * 40)
        lines.append(f"  Moyenne               : {self.average():.2f}/20")
        lines.append(f"  Mention               : {self.mention()}")
        lines.append(f"  Résultat              : {'Admis' if self.is_passing() else 'Ajourné'}")
        return "\n".join(lines)


class GradeBook:
    def __init__(self):
        self._students: dict[str, Student] = {}

    def add_student(self, name: str, student_id: str) -> Student:
        if student_id in self._students:
            raise ValueError(f"Student with ID '{student_id}' already exists")
        student = Student(name, student_id)
        self._students[student_id] = student
        return student

    def get_student(self, student_id: str) -> Student:
        if student_id not in self._students:
            raise KeyError(f"Student '{student_id}' not found")
        return self._students[student_id]

    def remove_student(self, student_id: str) -> None:
        if student_id not in self._students:
            raise KeyError(f"Student '{student_id}' not found")
        del self._students[student_id]

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

    def passing_students(self) -> list[Student]:
        return [s for s in self._students.values() if s.is_passing()]

    def failing_students(self) -> list[Student]:
        return [s for s in self._students.values() if not s.is_passing()]

    def summary(self) -> str:
        students = self.all_students()
        if not students:
            return "Aucun étudiant enregistré."
        passing = self.passing_students()
        failing = self.failing_students()
        lines = [
            "=" * 40,
            "       RÉCAPITULATIF DE CLASSE",
            "=" * 40,
            f"  Nombre d'étudiants : {len(students)}",
            f"  Moyenne de classe  : {self.class_average():.2f}/20",
            f"  Admis              : {len(passing)}",
            f"  Ajournés           : {len(failing)}",
        ]
        top = self.top_student()
        if top:
            lines.append(f"  Major de classe    : {top.name} ({top.average():.2f}/20)")
        lines.append("=" * 40)
        return "\n".join(lines)
