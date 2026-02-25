"""
Unit tests for the Student Grade Management System.
Run with:  python -m pytest test_grades.py -v
"""

import pytest
from grades import GradeBook, Student


# ---------------------------------------------------------------------------
# Student tests
# ---------------------------------------------------------------------------


class TestStudent:
    def test_creation(self):
        s = Student("Alice", "S001")
        assert s.name == "Alice"
        assert s.student_id == "S001"
        assert s.grades == {}

    def test_add_grade(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 15.0)
        assert s.grades["Math"] == [15.0]

    def test_add_multiple_grades_same_subject(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 12.0)
        s.add_grade("Math", 18.0)
        assert s.grades["Math"] == [12.0, 18.0]

    def test_add_grade_invalid_too_high(self):
        s = Student("Alice", "S001")
        with pytest.raises(ValueError):
            s.add_grade("Math", 21.0)

    def test_add_grade_invalid_negative(self):
        s = Student("Alice", "S001")
        with pytest.raises(ValueError):
            s.add_grade("Math", -1.0)

    def test_add_grade_boundary(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 0.0)
        s.add_grade("Math", 20.0)
        assert s.grades["Math"] == [0.0, 20.0]

    def test_average_subject(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 12.0)
        s.add_grade("Math", 18.0)
        assert s.average("Math") == 15.0

    def test_average_overall(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 16.0)
        s.add_grade("Physics", 14.0)
        assert s.average() == 15.0

    def test_average_no_grades(self):
        s = Student("Alice", "S001")
        assert s.average() == 0.0
        assert s.average("Math") == 0.0

    def test_average_unknown_subject(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 15.0)
        assert s.average("Physics") == 0.0

    def test_mention_tres_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 16.0)
        assert s.mention() == "Très Bien"

    def test_mention_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 14.0)
        assert s.mention() == "Bien"

    def test_mention_assez_bien(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 12.0)
        assert s.mention() == "Assez Bien"

    def test_mention_passable(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 10.0)
        assert s.mention() == "Passable"

    def test_mention_insuffisant(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 8.0)
        assert s.mention() == "Insuffisant"

    def test_serialization_round_trip(self):
        s = Student("Alice", "S001")
        s.add_grade("Math", 15.0)
        s.add_grade("Physics", 12.0)
        restored = Student.from_dict(s.to_dict())
        assert restored.name == s.name
        assert restored.student_id == s.student_id
        assert restored.grades == s.grades


# ---------------------------------------------------------------------------
# GradeBook tests
# ---------------------------------------------------------------------------


class TestGradeBook:
    def setup_method(self):
        self.book = GradeBook()
        self.alice = Student("Alice", "S001")
        self.bob = Student("Bob", "S002")
        self.alice.add_grade("Math", 16.0)
        self.alice.add_grade("Physics", 14.0)
        self.bob.add_grade("Math", 10.0)
        self.bob.add_grade("Physics", 12.0)

    def test_add_student(self):
        self.book.add_student(self.alice)
        assert self.book.get_student("S001") is self.alice

    def test_add_duplicate_student_raises(self):
        self.book.add_student(self.alice)
        with pytest.raises(ValueError):
            self.book.add_student(self.alice)

    def test_get_nonexistent_student(self):
        assert self.book.get_student("UNKNOWN") is None

    def test_remove_student(self):
        self.book.add_student(self.alice)
        assert self.book.remove_student("S001") is True
        assert self.book.get_student("S001") is None

    def test_remove_nonexistent_student(self):
        assert self.book.remove_student("UNKNOWN") is False

    def test_class_average(self):
        self.book.add_student(self.alice)
        self.book.add_student(self.bob)
        # Alice avg = 15.0, Bob avg = 11.0  =>  class avg = 13.0
        assert self.book.class_average() == 13.0

    def test_class_average_by_subject(self):
        self.book.add_student(self.alice)
        self.book.add_student(self.bob)
        # Alice Math=16, Bob Math=10 => avg 13.0
        assert self.book.class_average("Math") == 13.0

    def test_class_average_empty(self):
        assert self.book.class_average() == 0.0

    def test_ranking(self):
        self.book.add_student(self.alice)
        self.book.add_student(self.bob)
        ranked = self.book.ranking()
        assert ranked[0].student_id == "S001"  # Alice has higher avg
        assert ranked[1].student_id == "S002"

    def test_top_student(self):
        self.book.add_student(self.alice)
        self.book.add_student(self.bob)
        assert self.book.top_student().student_id == "S001"

    def test_top_student_empty(self):
        assert self.book.top_student() is None

    def test_serialization_round_trip(self):
        self.book.add_student(self.alice)
        self.book.add_student(self.bob)
        restored = GradeBook.from_dict(self.book.to_dict())
        assert set(restored.students.keys()) == {"S001", "S002"}
        assert restored.get_student("S001").grades == self.alice.grades
