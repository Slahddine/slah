import pytest
from grades import Student, GradeBook


# ── Student tests ──────────────────────────────────────────────────────────────

class TestStudent:
    def test_add_grade(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 15.0)
        assert s.grades["Math"] == 15.0

    def test_add_grade_overwrites(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 15.0)
        s.add_grade("Math", 18.0)
        assert s.grades["Math"] == 18.0

    def test_add_grade_invalid_high(self):
        s = Student("001", "Alice")
        with pytest.raises(ValueError):
            s.add_grade("Math", 21.0)

    def test_add_grade_invalid_low(self):
        s = Student("001", "Alice")
        with pytest.raises(ValueError):
            s.add_grade("Math", -1.0)

    def test_add_grade_boundary(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 0.0)
        s.add_grade("Physics", 20.0)
        assert s.grades["Math"] == 0.0
        assert s.grades["Physics"] == 20.0

    def test_remove_grade(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 15.0)
        s.remove_grade("Math")
        assert "Math" not in s.grades

    def test_remove_grade_not_found(self):
        s = Student("001", "Alice")
        with pytest.raises(KeyError):
            s.remove_grade("Math")

    def test_average_no_grades(self):
        s = Student("001", "Alice")
        assert s.average() == 0.0

    def test_average(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 14.0)
        s.add_grade("Physics", 16.0)
        assert s.average() == 15.0

    def test_mention_tres_bien(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 18.0)
        assert s.mention() == "Très Bien"

    def test_mention_bien(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 14.0)
        assert s.mention() == "Bien"

    def test_mention_assez_bien(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 12.0)
        assert s.mention() == "Assez Bien"

    def test_mention_passable(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 10.0)
        assert s.mention() == "Passable"

    def test_mention_insuffisant(self):
        s = Student("001", "Alice")
        s.add_grade("Math", 8.0)
        assert s.mention() == "Insuffisant"


# ── GradeBook tests ────────────────────────────────────────────────────────────

class TestGradeBook:
    def test_add_student(self):
        book = GradeBook()
        student = book.add_student("001", "Alice")
        assert student.name == "Alice"

    def test_add_duplicate_student(self):
        book = GradeBook()
        book.add_student("001", "Alice")
        with pytest.raises(ValueError):
            book.add_student("001", "Bob")

    def test_remove_student(self):
        book = GradeBook()
        book.add_student("001", "Alice")
        book.remove_student("001")
        assert book.all_students() == []

    def test_remove_nonexistent_student(self):
        book = GradeBook()
        with pytest.raises(KeyError):
            book.remove_student("999")

    def test_get_student(self):
        book = GradeBook()
        book.add_student("001", "Alice")
        student = book.get_student("001")
        assert student.name == "Alice"

    def test_get_nonexistent_student(self):
        book = GradeBook()
        with pytest.raises(KeyError):
            book.get_student("999")

    def test_all_students(self):
        book = GradeBook()
        book.add_student("001", "Alice")
        book.add_student("002", "Bob")
        assert len(book.all_students()) == 2

    def test_class_average_empty(self):
        book = GradeBook()
        assert book.class_average() == 0.0

    def test_class_average(self):
        book = GradeBook()
        s1 = book.add_student("001", "Alice")
        s1.add_grade("Math", 10.0)
        s2 = book.add_student("002", "Bob")
        s2.add_grade("Math", 20.0)
        assert book.class_average() == 15.0

    def test_top_student_empty(self):
        book = GradeBook()
        assert book.top_student() is None

    def test_top_student(self):
        book = GradeBook()
        s1 = book.add_student("001", "Alice")
        s1.add_grade("Math", 10.0)
        s2 = book.add_student("002", "Bob")
        s2.add_grade("Math", 18.0)
        assert book.top_student().name == "Bob"

    def test_ranking(self):
        book = GradeBook()
        s1 = book.add_student("001", "Alice")
        s1.add_grade("Math", 12.0)
        s2 = book.add_student("002", "Bob")
        s2.add_grade("Math", 18.0)
        s3 = book.add_student("003", "Charlie")
        s3.add_grade("Math", 15.0)
        ranking = book.ranking()
        assert [s.name for s in ranking] == ["Bob", "Charlie", "Alice"]
