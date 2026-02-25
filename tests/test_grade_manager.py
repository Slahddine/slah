import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from student import Student
from grade_manager import GradeManager


# ── Student tests ──────────────────────────────────────────────────────────────

class TestStudent:
    def test_create_student(self):
        s = Student("Ali")
        assert s.name == "Ali"
        assert s.grades == {}

    def test_create_student_strips_whitespace(self):
        s = Student("  Sara  ")
        assert s.name == "Sara"

    def test_create_student_empty_name_raises(self):
        with pytest.raises(ValueError):
            Student("")

    def test_add_grade(self):
        s = Student("Ali")
        s.add_grade("Maths", 15.0)
        assert s.grades["Maths"] == [15.0]

    def test_add_multiple_grades_same_subject(self):
        s = Student("Ali")
        s.add_grade("Maths", 14.0)
        s.add_grade("Maths", 16.0)
        assert s.grades["Maths"] == [14.0, 16.0]

    def test_add_grade_invalid_range(self):
        s = Student("Ali")
        with pytest.raises(ValueError):
            s.add_grade("Maths", 21.0)
        with pytest.raises(ValueError):
            s.add_grade("Maths", -1.0)

    def test_add_grade_empty_subject_raises(self):
        s = Student("Ali")
        with pytest.raises(ValueError):
            s.add_grade("", 10.0)

    def test_average_no_grades(self):
        s = Student("Ali")
        assert s.average() == 0.0

    def test_average_single_grade(self):
        s = Student("Ali")
        s.add_grade("Maths", 18.0)
        assert s.average() == 18.0

    def test_average_multiple_subjects(self):
        s = Student("Ali")
        s.add_grade("Maths", 14.0)
        s.add_grade("Info", 16.0)
        assert s.average() == 15.0

    def test_subject_average(self):
        s = Student("Ali")
        s.add_grade("Maths", 10.0)
        s.add_grade("Maths", 20.0)
        assert s.subject_average("Maths") == 15.0

    def test_subject_average_unknown_subject(self):
        s = Student("Ali")
        assert s.subject_average("Physique") == 0.0

    def test_report_no_grades(self):
        s = Student("Ali")
        report = s.report()
        assert "Ali" in report
        assert "Aucune note" in report

    def test_report_with_grades(self):
        s = Student("Ali")
        s.add_grade("Maths", 15.0)
        report = s.report()
        assert "Maths" in report
        assert "15.0" in report


# ── GradeManager tests ────────────────────────────────────────────────────────

class TestGradeManager:
    def setup_method(self):
        self.manager = GradeManager()

    def test_add_student(self):
        self.manager.add_student("Ali")
        assert self.manager.get_student("Ali").name == "Ali"

    def test_add_duplicate_student_raises(self):
        self.manager.add_student("Ali")
        with pytest.raises(ValueError):
            self.manager.add_student("Ali")

    def test_add_student_case_insensitive_duplicate(self):
        self.manager.add_student("Ali")
        with pytest.raises(ValueError):
            self.manager.add_student("ALI")

    def test_remove_student(self):
        self.manager.add_student("Ali")
        self.manager.remove_student("Ali")
        with pytest.raises(KeyError):
            self.manager.get_student("Ali")

    def test_remove_nonexistent_student_raises(self):
        with pytest.raises(KeyError):
            self.manager.remove_student("Ghost")

    def test_get_nonexistent_student_raises(self):
        with pytest.raises(KeyError):
            self.manager.get_student("Nobody")

    def test_add_grade(self):
        self.manager.add_student("Ali")
        self.manager.add_grade("Ali", "Maths", 17.0)
        student = self.manager.get_student("Ali")
        assert student.grades["Maths"] == [17.0]

    def test_all_students_sorted(self):
        self.manager.add_student("Zied")
        self.manager.add_student("Ali")
        self.manager.add_student("Meriem")
        names = [s.name for s in self.manager.all_students()]
        assert names == ["Ali", "Meriem", "Zied"]

    def test_best_student(self):
        self.manager.add_student("Ali")
        self.manager.add_grade("Ali", "Maths", 10.0)
        self.manager.add_student("Sara")
        self.manager.add_grade("Sara", "Maths", 18.0)
        best = self.manager.best_student()
        assert best.name == "Sara"

    def test_best_student_empty_manager(self):
        assert self.manager.best_student() is None

    def test_class_average(self):
        self.manager.add_student("Ali")
        self.manager.add_grade("Ali", "Maths", 10.0)
        self.manager.add_student("Sara")
        self.manager.add_grade("Sara", "Maths", 20.0)
        assert self.manager.class_average() == 15.0

    def test_class_average_empty(self):
        assert self.manager.class_average() == 0.0

    def test_full_report_empty(self):
        report = self.manager.full_report()
        assert "Aucun étudiant" in report

    def test_full_report_with_students(self):
        self.manager.add_student("Ali")
        self.manager.add_grade("Ali", "Maths", 16.0)
        report = self.manager.full_report()
        assert "Ali" in report
        assert "Maths" in report
        assert "Meilleur étudiant" in report
