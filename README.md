# Système de Gestion des Notes Étudiants

> **Idée de projet informatique** — un système complet de gestion des notes pour une classe.

## Description

Cette application en ligne de commande (CLI) permet de gérer les notes d'étudiants :
- Ajouter / supprimer des étudiants
- Enregistrer / modifier / supprimer des notes par matière
- Calculer les moyennes individuelles et la moyenne de classe
- Afficher le classement et la mention (Très Bien, Bien, Assez Bien, Passable, Insuffisant)

## Structure du projet

```
├── grades.py        # Modèle de données : Student et GradeBook
├── main.py          # Interface en ligne de commande interactive
├── test_grades.py   # Tests unitaires (pytest)
└── README.md
```

## Prérequis

- Python 3.10+
- `pytest` pour les tests

```bash
pip install pytest
```

## Lancer l'application

```bash
python main.py
```

Exemple de session :

```
=== Gestion des Notes Étudiants ===
1. Ajouter un étudiant
2. Supprimer un étudiant
3. Ajouter / modifier une note
4. Supprimer une note
5. Afficher les notes d'un étudiant
6. Afficher le classement de la classe
7. Afficher la moyenne de la classe
8. Afficher le meilleur étudiant
0. Quitter
--------------------------------------------------
Votre choix : 1
ID étudiant : 001
Nom complet : Ahmed Ben Ali
✓ Étudiant 'Ahmed Ben Ali' ajouté avec succès.
```

## Lancer les tests

```bash
pytest test_grades.py -v
```

## Système de mention

| Moyenne        | Mention       |
|----------------|---------------|
| ≥ 16/20        | Très Bien     |
| ≥ 14/20        | Bien          |
| ≥ 12/20        | Assez Bien    |
| ≥ 10/20        | Passable      |
| < 10/20        | Insuffisant   |
