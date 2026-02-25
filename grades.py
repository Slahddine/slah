"""Student Grade Management System - Core module."""

import json
import os
from typing import Dict, List, Optional

DATA_FILE = "students.json"


def load_data() -> Dict:
    """Load student data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_data(data: Dict) -> None:
    """Save student data to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_student(name: str) -> str:
    """Add a new student. Returns a message."""
    data = load_data()
    if name in data:
        return f"L'étudiant '{name}' existe déjà."
    data[name] = []
    save_data(data)
    return f"Étudiant '{name}' ajouté avec succès."


def remove_student(name: str) -> str:
    """Remove a student. Returns a message."""
    data = load_data()
    if name not in data:
        return f"Étudiant '{name}' introuvable."
    del data[name]
    save_data(data)
    return f"Étudiant '{name}' supprimé avec succès."


def add_grade(name: str, subject: str, grade: float) -> str:
    """Add a grade for a student. Returns a message."""
    if not (0 <= grade <= 20):
        return "La note doit être comprise entre 0 et 20."
    data = load_data()
    if name not in data:
        return f"Étudiant '{name}' introuvable."
    data[name].append({"matière": subject, "note": grade})
    save_data(data)
    return f"Note {grade}/20 en '{subject}' ajoutée pour '{name}'."


def get_stats(name: str) -> Optional[Dict]:
    """Return statistics for a student, or None if not found."""
    data = load_data()
    if name not in data:
        return None
    grades = [entry["note"] for entry in data[name]]
    if not grades:
        return {"name": name, "grades": [], "average": None,
                "min": None, "max": None, "status": "Aucune note"}
    average = sum(grades) / len(grades)
    return {
        "name": name,
        "grades": data[name],
        "average": round(average, 2),
        "min": min(grades),
        "max": max(grades),
        "status": "Admis" if average >= 10 else "Ajourné",
    }


def list_students() -> List[str]:
    """Return a list of all student names."""
    return list(load_data().keys())
