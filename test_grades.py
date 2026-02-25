"""Tests for the Student Grade Management System."""

import os
import sys
import unittest

# Point to repo root so we can import grades module
sys.path.insert(0, os.path.dirname(__file__))

import grades


class TestGradeManagement(unittest.TestCase):

    def setUp(self):
        """Use a temporary data file for tests."""
        grades.DATA_FILE = "/tmp/test_students.json"
        # Clean up before each test
        if os.path.exists(grades.DATA_FILE):
            os.remove(grades.DATA_FILE)

    def tearDown(self):
        if os.path.exists(grades.DATA_FILE):
            os.remove(grades.DATA_FILE)

    # --- add_student ---

    def test_add_student_success(self):
        msg = grades.add_student("Alice")
        self.assertIn("Alice", msg)
        self.assertIn("Alice", grades.list_students())

    def test_add_student_duplicate(self):
        grades.add_student("Bob")
        msg = grades.add_student("Bob")
        self.assertIn("existe déjà", msg)

    # --- remove_student ---

    def test_remove_student_success(self):
        grades.add_student("Charlie")
        msg = grades.remove_student("Charlie")
        self.assertIn("supprimé", msg)
        self.assertNotIn("Charlie", grades.list_students())

    def test_remove_student_not_found(self):
        msg = grades.remove_student("Unknown")
        self.assertIn("introuvable", msg)

    # --- add_grade ---

    def test_add_grade_success(self):
        grades.add_student("Diana")
        msg = grades.add_grade("Diana", "Maths", 15.5)
        self.assertIn("15.5", msg)

    def test_add_grade_invalid_range_high(self):
        grades.add_student("Eve")
        msg = grades.add_grade("Eve", "Maths", 21)
        self.assertIn("entre 0 et 20", msg)

    def test_add_grade_invalid_range_low(self):
        grades.add_student("Eve")
        msg = grades.add_grade("Eve", "Maths", -1)
        self.assertIn("entre 0 et 20", msg)

    def test_add_grade_student_not_found(self):
        msg = grades.add_grade("Ghost", "Maths", 10)
        self.assertIn("introuvable", msg)

    # --- get_stats ---

    def test_get_stats_no_grades(self):
        grades.add_student("Frank")
        stats = grades.get_stats("Frank")
        self.assertEqual(stats["average"], None)
        self.assertEqual(stats["status"], "Aucune note")

    def test_get_stats_passing(self):
        grades.add_student("Grace")
        grades.add_grade("Grace", "Maths", 12)
        grades.add_grade("Grace", "Physics", 14)
        stats = grades.get_stats("Grace")
        self.assertEqual(stats["average"], 13.0)
        self.assertEqual(stats["status"], "Admis")
        self.assertEqual(stats["min"], 12)
        self.assertEqual(stats["max"], 14)

    def test_get_stats_failing(self):
        grades.add_student("Hank")
        grades.add_grade("Hank", "Maths", 8)
        grades.add_grade("Hank", "History", 6)
        stats = grades.get_stats("Hank")
        self.assertEqual(stats["status"], "Ajourné")

    def test_get_stats_not_found(self):
        result = grades.get_stats("Nobody")
        self.assertIsNone(result)

    # --- list_students ---

    def test_list_students_empty(self):
        self.assertEqual(grades.list_students(), [])

    def test_list_students_multiple(self):
        grades.add_student("Iris")
        grades.add_student("Jack")
        students = grades.list_students()
        self.assertIn("Iris", students)
        self.assertIn("Jack", students)


if __name__ == "__main__":
    unittest.main()
