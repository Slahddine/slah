#!/usr/bin/env python3
"""
Student Grade Management System — CLI
Système de gestion des notes étudiants
Usage: python app.py
"""

from students import GradeBook


def print_menu() -> None:
    print("\n=== Système de Gestion des Notes ===")
    print("1. Ajouter un étudiant")
    print("2. Ajouter une note")
    print("3. Afficher les notes d'un étudiant")
    print("4. Rapport complet de la classe")
    print("5. Top 3 étudiants")
    print("6. Supprimer un étudiant")
    print("0. Quitter")
    print("=====================================")


def main() -> None:
    book = GradeBook()

    # Pre-load some sample data so the app is usable immediately
    sample_data = [
        ("Alice Dupont", "S001"),
        ("Bob Martin", "S002"),
        ("Chloé Bernard", "S003"),
    ]
    sample_grades = {
        "S001": {"Maths": 17.5, "Physique": 15.0, "Informatique": 18.0},
        "S002": {"Maths": 12.0, "Physique": 11.5, "Informatique": 13.5},
        "S003": {"Maths": 14.0, "Physique": 16.0, "Informatique": 15.5},
    }
    for name, sid in sample_data:
        s = book.add_student(name, sid)
        for subject, grade in sample_grades[sid].items():
            s.add_grade(subject, grade)

    print("Bienvenue dans le Système de Gestion des Notes!")
    print("(Données d'exemple chargées: Alice, Bob, Chloé)")

    while True:
        print_menu()
        choice = input("Votre choix: ").strip()

        if choice == "1":
            name = input("Nom de l'étudiant: ").strip()
            sid = input("Numéro étudiant: ").strip()
            try:
                book.add_student(name, sid)
                print(f"✓ Étudiant '{name}' ajouté avec succès.")
            except ValueError as e:
                print(f"Erreur: {e}")

        elif choice == "2":
            sid = input("Numéro étudiant: ").strip()
            try:
                student = book.get_student(sid)
                subject = input("Matière: ").strip()
                grade = float(input("Note (0-20): ").strip())
                student.add_grade(subject, grade)
                print(f"✓ Note ajoutée pour {student.name} en {subject}: {grade}/20")
            except (KeyError, ValueError) as e:
                print(f"Erreur: {e}")

        elif choice == "3":
            sid = input("Numéro étudiant: ").strip()
            try:
                student = book.get_student(sid)
                print(f"\nÉtudiant : {student.name}  (ID: {student.student_id})")
                if student.grades:
                    for subject, grade in sorted(student.grades.items()):
                        print(f"  {subject:<20} {grade:>5.2f}/20")
                    print(f"  {'Moyenne':<20} {student.average():>5.2f}/20  — {student.mention()}")
                else:
                    print("  Aucune note enregistrée.")
            except KeyError as e:
                print(f"Erreur: {e}")

        elif choice == "4":
            print(book.report())

        elif choice == "5":
            top = book.top_students(3)
            print("\n🏆 Top 3 Étudiants:")
            for i, student in enumerate(top, 1):
                print(f"  {i}. {student.name} — {student.average():.2f}/20 ({student.mention()})")

        elif choice == "6":
            sid = input("Numéro étudiant à supprimer: ").strip()
            try:
                student = book.get_student(sid)
                confirm = input(f"Supprimer '{student.name}' ? (o/n): ").strip().lower()
                if confirm == "o":
                    book.remove_student(sid)
                    print(f"✓ Étudiant '{student.name}' supprimé.")
                else:
                    print("Annulé.")
            except KeyError as e:
                print(f"Erreur: {e}")

        elif choice == "0":
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
