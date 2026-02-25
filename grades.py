"""
Système de Gestion des Notes (Student Grade Management System)
A simple command-line application to manage student grades.
"""

import json
import os

DATA_FILE = "students.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_student(data, name):
    if name in data:
        print(f"L'étudiant '{name}' existe déjà.")
    else:
        data[name] = []
        save_data(data)
        print(f"Étudiant '{name}' ajouté avec succès.")


def add_grade(data, name, subject, grade):
    if name not in data:
        print(f"Étudiant '{name}' introuvable.")
        return
    if not (0 <= grade <= 20):
        print("La note doit être entre 0 et 20.")
        return
    data[name].append({"matière": subject, "note": grade})
    save_data(data)
    print(f"Note {grade}/20 en '{subject}' ajoutée pour '{name}'.")


def get_average(grades):
    if not grades:
        return 0.0
    return sum(g["note"] for g in grades) / len(grades)


def get_mention(average):
    if average >= 16:
        return "Très Bien"
    elif average >= 14:
        return "Bien"
    elif average >= 12:
        return "Assez Bien"
    elif average >= 10:
        return "Passable"
    else:
        return "Insuffisant"


def show_student(data, name):
    if name not in data:
        print(f"Étudiant '{name}' introuvable.")
        return
    grades = data[name]
    print(f"\n--- Résultats de {name} ---")
    if not grades:
        print("Aucune note enregistrée.")
        return
    for entry in grades:
        print(f"  {entry['matière']}: {entry['note']}/20")
    avg = get_average(grades)
    mention = get_mention(avg)
    print(f"  Moyenne: {avg:.2f}/20  ({mention})")


def show_all(data):
    if not data:
        print("Aucun étudiant enregistré.")
        return
    print("\n=== Classement des étudiants ===")
    ranking = sorted(data.items(), key=lambda x: get_average(x[1]), reverse=True)
    for rank, (name, grades) in enumerate(ranking, start=1):
        avg = get_average(grades)
        mention = get_mention(avg)
        print(f"  {rank}. {name}: {avg:.2f}/20 ({mention})")


def remove_student(data, name):
    if name not in data:
        print(f"Étudiant '{name}' introuvable.")
        return
    del data[name]
    save_data(data)
    print(f"Étudiant '{name}' supprimé.")


def main():
    data = load_data()
    print("=== Système de Gestion des Notes ===")
    while True:
        print("\nMenu:")
        print("  1. Ajouter un étudiant")
        print("  2. Ajouter une note")
        print("  3. Afficher les notes d'un étudiant")
        print("  4. Afficher le classement")
        print("  5. Supprimer un étudiant")
        print("  0. Quitter")
        choice = input("Votre choix: ").strip()

        if choice == "1":
            name = input("Nom de l'étudiant: ").strip()
            add_student(data, name)
        elif choice == "2":
            name = input("Nom de l'étudiant: ").strip()
            subject = input("Matière: ").strip()
            try:
                grade = float(input("Note (0-20): ").strip())
            except ValueError:
                print("Note invalide.")
                continue
            add_grade(data, name, subject, grade)
        elif choice == "3":
            name = input("Nom de l'étudiant: ").strip()
            show_student(data, name)
        elif choice == "4":
            show_all(data)
        elif choice == "5":
            name = input("Nom de l'étudiant: ").strip()
            remove_student(data, name)
        elif choice == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
