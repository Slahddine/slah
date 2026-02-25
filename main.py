"""Student Grade Management System - CLI interface."""

from grades import (
    add_grade,
    add_student,
    get_stats,
    list_students,
    remove_student,
)


def print_menu():
    print("\n===== Gestion des Notes =====")
    print("1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Ajouter une note")
    print("4. Voir les résultats d'un étudiant")
    print("5. Liste des étudiants")
    print("0. Quitter")
    print("==============================")


def main():
    while True:
        print_menu()
        choice = input("Votre choix: ").strip()

        if choice == "1":
            name = input("Nom de l'étudiant: ").strip()
            if name:
                print(add_student(name))

        elif choice == "2":
            name = input("Nom de l'étudiant à supprimer: ").strip()
            if name:
                print(remove_student(name))

        elif choice == "3":
            name = input("Nom de l'étudiant: ").strip()
            subject = input("Matière: ").strip()
            try:
                grade = float(input("Note (0-20): ").strip())
                print(add_grade(name, subject, grade))
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        elif choice == "4":
            name = input("Nom de l'étudiant: ").strip()
            stats = get_stats(name)
            if stats is None:
                print(f"Étudiant '{name}' introuvable.")
            else:
                print(f"\n--- Résultats de {stats['name']} ---")
                if stats["grades"]:
                    for entry in stats["grades"]:
                        print(f"  {entry['matière']}: {entry['note']}/20")
                    print(f"  Moyenne : {stats['average']}/20")
                    print(f"  Min : {stats['min']} | Max : {stats['max']}")
                    print(f"  Statut  : {stats['status']}")
                else:
                    print("  Aucune note enregistrée.")

        elif choice == "5":
            students = list_students()
            if students:
                print("\nÉtudiants inscrits :")
                for s in students:
                    print(f"  - {s}")
            else:
                print("Aucun étudiant enregistré.")

        elif choice == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
