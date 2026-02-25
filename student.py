class Student:
    """Represents a student with a name and grades per subject."""

    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.name = name.strip()
        self.grades: dict[str, list[float]] = {}

    def add_grade(self, subject: str, grade: float):
        """Add a grade for a subject (0–20 scale)."""
        if not subject or not subject.strip():
            raise ValueError("Subject name cannot be empty.")
        if not (0 <= grade <= 20):
            raise ValueError("Grade must be between 0 and 20.")
        subject = subject.strip()
        self.grades.setdefault(subject, []).append(grade)

    def average(self) -> float:
        """Return the overall average across all subjects."""
        all_grades = [g for grades in self.grades.values() for g in grades]
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 2)

    def subject_average(self, subject: str) -> float:
        """Return the average for a specific subject."""
        subject = subject.strip()
        grades = self.grades.get(subject, [])
        if not grades:
            return 0.0
        return round(sum(grades) / len(grades), 2)

    def report(self) -> str:
        """Return a formatted grade report for this student."""
        lines = [f"Étudiant : {self.name}"]
        if not self.grades:
            lines.append("  Aucune note enregistrée.")
        else:
            for subject, grades in self.grades.items():
                avg = self.subject_average(subject)
                grades_str = ", ".join(str(g) for g in grades)
                lines.append(f"  {subject}: {grades_str}  (moyenne: {avg})")
            lines.append(f"  Moyenne générale : {self.average()}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, average={self.average()})"
