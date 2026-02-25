#!/usr/bin/env python3
"""
Système de Gestion des Notes Étudiantes — Interface en ligne de commande
Student Grade Management System — Command-Line Interface
"""

import json
import os

from grades import GradeBook, Student

DATA_FILE = "gradebook.json"


def load_gradebook() -> GradeBook:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return GradeBook.from_dict(json.load(f))
    return GradeBook()


def save_gradebook(book: GradeBook) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(book.to_dict(), f, ensure_ascii=False, indent=2)


def print_menu() -> None:
    print("\n" + "=" * 45)
    print("  Système de Gestion des Notes Étudiantes")
    print("=" * 45)
    print("  1. Ajouter un étudiant")
    print("  2. Saisir une note")
    print("  3. Afficher les notes d'un étudiant")
    print("  4. Afficher le classement de la classe")
    print("  5. Moyenne générale de la classe")
    print("  6. Meilleur étudiant")
    print("  7. Supprimer un étudiant")
    print("  0. Quitter")
    print("=" * 45)


def add_student(book: GradeBook) -> None:
    name = input("Nom de l'étudiant : ").strip()
    sid = input("Numéro étudiant   : ").strip()
    if not name or not sid:
        print("⚠  Nom et numéro ne peuvent pas être vides.")
        return
    try:
        book.add_student(Student(name, sid))
        save_gradebook(book)
        print(f"✓ Étudiant {name!r} ajouté avec succès.")
    except ValueError as e:
        print(f"⚠  {e}")


def enter_grade(book: GradeBook) -> None:
    sid = input("Numéro étudiant : ").strip()
    student = book.get_student(sid)
    if student is None:
        print("⚠  Étudiant introuvable.")
        return
    subject = input("Matière         : ").strip()
    try:
        grade = float(input("Note (0-20)     : ").strip())
        student.add_grade(subject, grade)
        save_gradebook(book)
        print(f"✓ Note {grade} ajoutée en {subject!r} pour {student.name}.")
    except ValueError as e:
        print(f"⚠  {e}")


def show_student(book: GradeBook) -> None:
    sid = input("Numéro étudiant : ").strip()
    student = book.get_student(sid)
    if student is None:
        print("⚠  Étudiant introuvable.")
        return
    print(f"\n  Étudiant : {student.name}  (ID: {student.student_id})")
    print(f"  Mention  : {student.mention()}  |  Moyenne générale : {student.average()}/20")
    if student.grades:
        print("  ─" * 20)
        for subject, grades in student.grades.items():
            avg = student.average(subject)
            print(f"  {subject:<20} notes: {grades}  →  moy: {avg}/20")
    else:
        print("  Aucune note enregistrée.")


def show_ranking(book: GradeBook) -> None:
    ranked = book.ranking()
    if not ranked:
        print("⚠  Aucun étudiant enregistré.")
        return
    print(f"\n  {'Rang':<5} {'Nom':<20} {'ID':<10} {'Moyenne'}")
    print("  " + "─" * 45)
    for i, s in enumerate(ranked, 1):
        print(f"  {i:<5} {s.name:<20} {s.student_id:<10} {s.average()}/20  ({s.mention()})")


def show_class_average(book: GradeBook) -> None:
    avg = book.class_average()
    print(f"\n  Moyenne générale de la classe : {avg}/20")


def show_top_student(book: GradeBook) -> None:
    top = book.top_student()
    if top is None:
        print("⚠  Aucun étudiant enregistré.")
    else:
        print(f"\n  🏆 Meilleur étudiant : {top.name} (ID: {top.student_id}) — {top.average()}/20 ({top.mention()})")


def remove_student(book: GradeBook) -> None:
    sid = input("Numéro étudiant à supprimer : ").strip()
    if book.remove_student(sid):
        save_gradebook(book)
        print("✓ Étudiant supprimé.")
    else:
        print("⚠  Étudiant introuvable.")


def main() -> None:
    book = load_gradebook()
    actions = {
        "1": add_student,
        "2": enter_grade,
        "3": show_student,
        "4": show_ranking,
        "5": show_class_average,
        "6": show_top_student,
        "7": remove_student,
    }
    while True:
        print_menu()
        choice = input("Votre choix : ").strip()
        if choice == "0":
            print("À bientôt !")
            break
        action = actions.get(choice)
        if action:
            action(book)
        else:
            print("⚠  Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
