"""
Gestionnaire de Notes Étudiantes — Interface en ligne de commande
Usage: python main.py
"""

from grades import (
    add_student,
    add_grade,
    get_student_report,
    list_students,
    get_class_ranking,
)


def print_separator():
    print("-" * 40)


def print_menu():
    print_separator()
    print("  Gestionnaire de Notes Étudiantes")
    print_separator()
    print("1. Ajouter un étudiant")
    print("2. Ajouter une note")
    print("3. Voir le bulletin d'un étudiant")
    print("4. Classement de la classe")
    print("5. Liste des étudiants")
    print("0. Quitter")
    print_separator()


def main():
    students = {}

    while True:
        print_menu()
        choice = input("Votre choix : ").strip()

        if choice == "1":
            name = input("Nom de l'étudiant : ").strip()
            try:
                add_student(students, name)
                print(f"✓ Étudiant '{name}' ajouté.")
            except ValueError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "2":
            name = input("Nom de l'étudiant : ").strip()
            try:
                grade_input = input("Note (0-20) : ").strip()
                grade = float(grade_input)
                add_grade(students, name, grade)
                print(f"✓ Note {grade} ajoutée pour '{name}'.")
            except ValueError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "3":
            name = input("Nom de l'étudiant : ").strip()
            try:
                report = get_student_report(students, name)
                print_separator()
                print(f"  Bulletin de {report['name']}")
                print_separator()
                if report["grades"]:
                    print(f"  Notes    : {report['grades']}")
                    print(f"  Moyenne  : {report['average']:.2f}/20")
                    print(f"  Mention  : {report['mention']}")
                else:
                    print("  Aucune note enregistrée.")
                print_separator()
            except ValueError as e:
                print(f"✗ Erreur : {e}")

        elif choice == "4":
            ranking = get_class_ranking(students)
            if not ranking:
                print("Aucun étudiant enregistré.")
            else:
                print_separator()
                print("  Classement")
                print_separator()
                for rank, (name, avg) in enumerate(ranking, start=1):
                    avg_str = f"{avg:.2f}" if avg >= 0 else "N/A"
                    print(f"  {rank}. {name} — {avg_str}/20")
                print_separator()

        elif choice == "5":
            names = list_students(students)
            if not names:
                print("Aucun étudiant enregistré.")
            else:
                print("Étudiants inscrits :", ", ".join(names))

        elif choice == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
