"""Unit tests for the Student Grade Management System."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from students import Student, GradeBook


class TestStudent:
    def test_add_grade(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 15.0)
        assert s.grades["Maths"] == 15.0

    def test_add_grade_updates_existing(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 15.0)
        s.add_grade("Maths", 18.0)
        assert s.grades["Maths"] == 18.0

    def test_add_grade_invalid_below_zero(self):
        s = Student("Alice", "S001")
        with pytest.raises(ValueError):
            s.add_grade("Maths", -1)

    def test_add_grade_invalid_above_twenty(self):
        s = Student("Alice", "S001")
        with pytest.raises(ValueError):
            s.add_grade("Maths", 21)

    def test_average_no_grades(self):
        s = Student("Alice", "S001")
        assert s.average() == 0.0

    def test_average_single_grade(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 15.0)
        assert s.average() == 15.0

    def test_average_multiple_grades(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 10.0)
        s.add_grade("Physique", 20.0)
        assert s.average() == 15.0

    def test_mention_tres_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 16.0)
        assert s.mention() == "Très Bien"

    def test_mention_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 14.0)
        assert s.mention() == "Bien"

    def test_mention_assez_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 12.0)
        assert s.mention() == "Assez Bien"

    def test_mention_passable(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 10.0)
        assert s.mention() == "Passable"

    def test_mention_insuffisant(self):
        s = Student("Alice", "S001")
        s.add_grade("Maths", 8.0)
        assert s.mention() == "Insuffisant"


class TestGradeBook:
    def setup_method(self):
        self.book = GradeBook()

    def test_add_student(self):
        s = self.book.add_student("Alice", "S001")
        assert s.name == "Alice"
        assert s.student_id == "S001"

    def test_add_duplicate_student_raises(self):
        self.book.add_student("Alice", "S001")
        with pytest.raises(ValueError):
            self.book.add_student("Alice Copy", "S001")

    def test_get_student(self):
        self.book.add_student("Alice", "S001")
        s = self.book.get_student("S001")
        assert s.name == "Alice"

    def test_get_missing_student_raises(self):
        with pytest.raises(KeyError):
            self.book.get_student("MISSING")

    def test_remove_student(self):
        self.book.add_student("Alice", "S001")
        self.book.remove_student("S001")
        with pytest.raises(KeyError):
            self.book.get_student("S001")

    def test_remove_missing_student_raises(self):
        with pytest.raises(KeyError):
            self.book.remove_student("MISSING")

    def test_all_students_sorted_by_name(self):
        self.book.add_student("Zoe", "S003")
        self.book.add_student("Alice", "S001")
        self.book.add_student("Bob", "S002")
        names = [s.name for s in self.book.all_students()]
        assert names == ["Alice", "Bob", "Zoe"]

    def test_class_average_empty(self):
        assert self.book.class_average() == 0.0

    def test_class_average(self):
        s1 = self.book.add_student("Alice", "S001")
        s2 = self.book.add_student("Bob", "S002")
        s1.add_grade("Maths", 20.0)
        s2.add_grade("Maths", 10.0)
        # Alice average=20, Bob average=10 → class average=15
        assert self.book.class_average() == 15.0

    def test_top_students(self):
        s1 = self.book.add_student("Alice", "S001")
        s2 = self.book.add_student("Bob", "S002")
        s3 = self.book.add_student("Chloé", "S003")
        s1.add_grade("Maths", 18.0)
        s2.add_grade("Maths", 12.0)
        s3.add_grade("Maths", 15.0)
        top = self.book.top_students(2)
        assert [s.name for s in top] == ["Alice", "Chloé"]

    def test_subject_average(self):
        s1 = self.book.add_student("Alice", "S001")
        s2 = self.book.add_student("Bob", "S002")
        s1.add_grade("Maths", 16.0)
        s2.add_grade("Maths", 14.0)
        assert self.book.subject_average("Maths") == 15.0

    def test_subject_average_no_grades(self):
        self.book.add_student("Alice", "S001")
        assert self.book.subject_average("Maths") == 0.0

    def test_report_empty(self):
        assert self.book.report() == "No students enrolled."

    def test_report_contains_student_name(self):
        s = self.book.add_student("Alice Dupont", "S001")
        s.add_grade("Maths", 15.0)
        report = self.book.report()
        assert "Alice Dupont" in report
        assert "15.00" in report
