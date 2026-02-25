from grade_manager import GradeManager


def print_menu():
    print("\n=== Système de Gestion des Notes ===")
    print("1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Ajouter une note")
    print("4. Afficher le relevé d'un étudiant")
    print("5. Afficher le relevé complet")
    print("6. Meilleur étudiant")
    print("0. Quitter")
    print("=====================================")


def main():
    manager = GradeManager()

    while True:
        print_menu()
        choice = input("Votre choix : ").strip()

        if choice == "1":
            name = input("Nom de l'étudiant : ").strip()
            try:
                manager.add_student(name)
                print(f"✅ Étudiant '{name}' ajouté.")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == "2":
            name = input("Nom de l'étudiant à supprimer : ").strip()
            try:
                manager.remove_student(name)
                print(f"✅ Étudiant '{name}' supprimé.")
            except KeyError as e:
                print(f"❌ {e}")

        elif choice == "3":
            name = input("Nom de l'étudiant : ").strip()
            subject = input("Matière : ").strip()
            try:
                grade = float(input("Note (0-20) : ").strip())
                manager.add_grade(name, subject, grade)
                print("✅ Note ajoutée.")
            except (ValueError, KeyError) as e:
                print(f"❌ {e}")

        elif choice == "4":
            name = input("Nom de l'étudiant : ").strip()
            try:
                student = manager.get_student(name)
                print(student.report())
            except KeyError as e:
                print(f"❌ {e}")

        elif choice == "5":
            print(manager.full_report())

        elif choice == "6":
            best = manager.best_student()
            if best:
                print(f"🏆 Meilleur étudiant : {best.name} avec {best.average()}/20")
            else:
                print("Aucun étudiant enregistré.")

        elif choice == "0":
            print("Au revoir! 👋")
            break

        else:
            print("❌ Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
