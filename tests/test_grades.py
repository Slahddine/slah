import pytest
from grades import Student, GradeBook


class TestStudent:
    def test_add_grade_valid(self):
        student = Student("Ali Ben Salah", "S001")
        student.add_grade("Mathématiques", 15.5)
        assert student.grades["Mathématiques"] == 15.5

    def test_add_grade_invalid_below_zero(self):
        student = Student("Ali Ben Salah", "S001")
        with pytest.raises(ValueError):
            student.add_grade("Mathématiques", -1)

    def test_add_grade_invalid_above_twenty(self):
        student = Student("Ali Ben Salah", "S001")
        with pytest.raises(ValueError):
            student.add_grade("Mathématiques", 21)

    def test_average_no_grades(self):
        student = Student("Ali Ben Salah", "S001")
        assert student.average() == 0.0

    def test_average_with_grades(self):
        student = Student("Ali Ben Salah", "S001")
        student.add_grade("Maths", 16)
        student.add_grade("Physique", 14)
        assert student.average() == 15.0

    def test_mention_tres_bien(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 18)
        assert student.mention() == "Très Bien"

    def test_mention_bien(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 14)
        assert student.mention() == "Bien"

    def test_mention_assez_bien(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 12)
        assert student.mention() == "Assez Bien"

    def test_mention_passable(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 10)
        assert student.mention() == "Passable"

    def test_mention_insuffisant(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 8)
        assert student.mention() == "Insuffisant"

    def test_is_passing_true(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 12)
        assert student.is_passing() is True

    def test_is_passing_false(self):
        student = Student("Ali", "S001")
        student.add_grade("Maths", 9)
        assert student.is_passing() is False

    def test_report_contains_name(self):
        student = Student("Sarra Trabelsi", "S002")
        student.add_grade("Informatique", 17)
        report = student.report()
        assert "Sarra Trabelsi" in report
        assert "Informatique" in report
        assert "Admis" in report


class TestGradeBook:
    def test_add_and_get_student(self):
        book = GradeBook()
        book.add_student("Omar Jebali", "S001")
        student = book.get_student("S001")
        assert student.name == "Omar Jebali"

    def test_add_duplicate_student_raises(self):
        book = GradeBook()
        book.add_student("Omar Jebali", "S001")
        with pytest.raises(ValueError):
            book.add_student("Other Name", "S001")

    def test_get_nonexistent_student_raises(self):
        book = GradeBook()
        with pytest.raises(KeyError):
            book.get_student("UNKNOWN")

    def test_remove_student(self):
        book = GradeBook()
        book.add_student("Omar Jebali", "S001")
        book.remove_student("S001")
        assert len(book.all_students()) == 0

    def test_remove_nonexistent_student_raises(self):
        book = GradeBook()
        with pytest.raises(KeyError):
            book.remove_student("UNKNOWN")

    def test_class_average(self):
        book = GradeBook()
        s1 = book.add_student("Ali", "S001")
        s2 = book.add_student("Sarra", "S002")
        s1.add_grade("Maths", 16)
        s2.add_grade("Maths", 12)
        assert book.class_average() == 14.0

    def test_class_average_empty(self):
        book = GradeBook()
        assert book.class_average() == 0.0

    def test_top_student(self):
        book = GradeBook()
        s1 = book.add_student("Ali", "S001")
        s2 = book.add_student("Sarra", "S002")
        s1.add_grade("Maths", 16)
        s2.add_grade("Maths", 18)
        assert book.top_student().name == "Sarra"

    def test_top_student_empty(self):
        book = GradeBook()
        assert book.top_student() is None

    def test_passing_and_failing_students(self):
        book = GradeBook()
        s1 = book.add_student("Ali", "S001")
        s2 = book.add_student("Sarra", "S002")
        s1.add_grade("Maths", 8)
        s2.add_grade("Maths", 14)
        assert len(book.passing_students()) == 1
        assert len(book.failing_students()) == 1

    def test_summary_contains_stats(self):
        book = GradeBook()
        s1 = book.add_student("Ali", "S001")
        s1.add_grade("Maths", 15)
        summary = book.summary()
        assert "Ali" in summary
        assert "15.00" in summary

    def test_summary_empty(self):
        book = GradeBook()
        assert book.summary() == "Aucun étudiant enregistré."
