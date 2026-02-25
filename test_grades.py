"""Unit tests for the Student Grade Manager (grades.py)."""

import pytest
from grades import (
    calculate_average,
    get_mention,
    add_student,
    add_grade,
    get_student_report,
    list_students,
    get_class_ranking,
)


# --- calculate_average ---

def test_calculate_average_normal():
    assert calculate_average([10, 14, 16]) == pytest.approx(40 / 3)


def test_calculate_average_single():
    assert calculate_average([15]) == 15.0


def test_calculate_average_empty():
    assert calculate_average([]) is None


# --- get_mention ---

def test_mention_tres_bien():
    assert get_mention(16) == "Très Bien"
    assert get_mention(20) == "Très Bien"


def test_mention_bien():
    assert get_mention(14) == "Bien"
    assert get_mention(15.9) == "Bien"


def test_mention_assez_bien():
    assert get_mention(12) == "Assez Bien"
    assert get_mention(13.9) == "Assez Bien"


def test_mention_passable():
    assert get_mention(10) == "Passable"
    assert get_mention(11.9) == "Passable"


def test_mention_insuffisant():
    assert get_mention(9.9) == "Insuffisant"
    assert get_mention(0) == "Insuffisant"


def test_mention_none():
    assert get_mention(None) == "Aucune note"


# --- add_student ---

def test_add_student():
    students = {}
    add_student(students, "Alice")
    assert "Alice" in students
    assert students["Alice"] == []


def test_add_student_duplicate():
    students = {}
    add_student(students, "Alice")
    with pytest.raises(ValueError, match="existe déjà"):
        add_student(students, "Alice")


# --- add_grade ---

def test_add_grade():
    students = {"Bob": []}
    add_grade(students, "Bob", 15)
    assert students["Bob"] == [15]


def test_add_grade_boundary():
    students = {"Bob": []}
    add_grade(students, "Bob", 0)
    add_grade(students, "Bob", 20)
    assert students["Bob"] == [0, 20]


def test_add_grade_invalid_high():
    students = {"Bob": []}
    with pytest.raises(ValueError, match="entre 0 et 20"):
        add_grade(students, "Bob", 21)


def test_add_grade_invalid_low():
    students = {"Bob": []}
    with pytest.raises(ValueError, match="entre 0 et 20"):
        add_grade(students, "Bob", -1)


def test_add_grade_unknown_student():
    students = {}
    with pytest.raises(ValueError, match="n'existe pas"):
        add_grade(students, "Unknown", 10)


# --- get_student_report ---

def test_get_student_report():
    students = {"Clara": [12, 14, 16]}
    report = get_student_report(students, "Clara")
    assert report["name"] == "Clara"
    assert report["grades"] == [12, 14, 16]
    assert report["average"] == pytest.approx(42 / 3)
    assert report["mention"] == "Bien"


def test_get_student_report_no_grades():
    students = {"Dana": []}
    report = get_student_report(students, "Dana")
    assert report["average"] is None
    assert report["mention"] == "Aucune note"


def test_get_student_report_unknown():
    with pytest.raises(ValueError, match="n'existe pas"):
        get_student_report({}, "Ghost")


# --- list_students ---

def test_list_students_sorted():
    students = {"Zara": [], "Alice": [], "Bob": []}
    assert list_students(students) == ["Alice", "Bob", "Zara"]


def test_list_students_empty():
    assert list_students({}) == []


# --- get_class_ranking ---

def test_get_class_ranking():
    students = {"Alice": [18, 20], "Bob": [10, 12], "Clara": [14, 16]}
    ranking = get_class_ranking(students)
    names = [name for name, _ in ranking]
    assert names == ["Alice", "Clara", "Bob"]


def test_get_class_ranking_empty():
    assert get_class_ranking({}) == []
