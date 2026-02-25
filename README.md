# Système de Gestion des Notes 📚

Un projet informatique simple en Python pour gérer les notes des étudiants.

## Fonctionnalités

- Ajouter / supprimer des étudiants
- Ajouter des notes par matière
- Calculer la moyenne générale d'un étudiant
- Afficher le relevé de notes
- Trouver le meilleur étudiant

## Installation

```bash
python -m pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

## Lancer les tests

```bash
python -m pytest tests/ -v
```

## Structure du projet

```
slah/
├── main.py          # Point d'entrée (menu interactif)
├── student.py       # Modèle étudiant
├── grade_manager.py # Logique de gestion
├── tests/
│   └── test_grade_manager.py
└── README.md
```
