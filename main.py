"""
Interactive CLI for the Student Grade Management System.
"""

from grades import GradeBook


def print_separator():
    print("-" * 50)


def display_menu():
    print("\n=== Gestion des Notes Étudiants ===")
    print("1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Ajouter / modifier une note")
    print("4. Supprimer une note")
    print("5. Afficher les notes d'un étudiant")
    print("6. Afficher le classement de la classe")
    print("7. Afficher la moyenne de la classe")
    print("8. Afficher le meilleur étudiant")
    print("0. Quitter")
    print_separator()


def display_student(student):
    print(f"\nÉtudiant : {student.name}  (ID: {student.student_id})")
    if student.grades:
        for subject, grade in student.grades.items():
            print(f"  {subject:<20} : {grade:.2f}/20")
        print(f"  {'Moyenne':<20} : {student.average():.2f}/20  — {student.mention()}")
    else:
        print("  Aucune note enregistrée.")


def main():
    book = GradeBook()

    while True:
        display_menu()
        choice = input("Votre choix : ").strip()

        if choice == "1":
            sid = input("ID étudiant : ").strip()
            name = input("Nom complet : ").strip()
            try:
                book.add_student(sid, name)
                print(f"✓ Étudiant '{name}' ajouté avec succès.")
            except ValueError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "2":
            sid = input("ID étudiant à supprimer : ").strip()
            try:
                book.remove_student(sid)
                print("✓ Étudiant supprimé.")
            except KeyError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "3":
            sid = input("ID étudiant : ").strip()
            try:
                student = book.get_student(sid)
                subject = input("Matière : ").strip()
                grade = float(input("Note (0-20) : ").strip())
                student.add_grade(subject, grade)
                print(f"✓ Note enregistrée : {subject} = {grade}/20")
            except (KeyError, ValueError) as e:
                print(f"✗ Erreur : {e}")

        elif choice == "4":
            sid = input("ID étudiant : ").strip()
            try:
                student = book.get_student(sid)
                subject = input("Matière à supprimer : ").strip()
                student.remove_grade(subject)
                print(f"✓ Note de '{subject}' supprimée.")
            except (KeyError, ValueError) as e:
                print(f"✗ Erreur : {e}")

        elif choice == "5":
            sid = input("ID étudiant : ").strip()
            try:
                student = book.get_student(sid)
                display_student(student)
            except KeyError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "6":
            ranking = book.ranking()
            if not ranking:
                print("Aucun étudiant enregistré.")
            else:
                print("\n=== Classement ===")
                for rank, student in enumerate(ranking, start=1):
                    print(f"  {rank}. {student.name:<25} {student.average():.2f}/20  — {student.mention()}")

        elif choice == "7":
            print(f"\nMoyenne de la classe : {book.class_average():.2f}/20")

        elif choice == "8":
            top = book.top_student()
            if top is None:
                print("Aucun étudiant enregistré.")
            else:
                print(f"\nMeilleur étudiant : {top.name}  (moyenne : {top.average():.2f}/20)")

        elif choice == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
