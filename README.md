# Système de Gestion des Notes Étudiants 🎓

Un projet Python simple de gestion des notes d'étudiants — idéal comme **projet informatique** de première année.

## Fonctionnalités

- Ajouter / supprimer des étudiants
- Enregistrer des notes par matière (sur 20)
- Calculer la moyenne individuelle et la mention
- Calculer la moyenne de classe et par matière
- Afficher un rapport complet
- Classer les meilleurs étudiants

## Structure du projet

```
slah/
├── app.py          # Interface en ligne de commande (CLI)
├── students.py     # Logique métier (Student, GradeBook)
├── tests/
│   └── test_students.py  # Tests unitaires
└── README.md
```

## Installation & Utilisation

Python 3.10+ requis.

```bash
# Lancer l'application interactive
python app.py

# Lancer les tests
python -m pytest tests/ -v
```

## Exemple de rapport

```
=======================================================
                   STUDENT REPORT
=======================================================
ID         Name                 Average Mention
-------------------------------------------------------
S003       Chloé Bernard          15.17 Bien
S001       Alice Dupont           16.83 Très Bien
S002       Bob Martin             12.33 Assez Bien
-------------------------------------------------------
Class average: 14.78 / 20
=======================================================
```

## Mentions

| Moyenne   | Mention        |
|-----------|----------------|
| ≥ 16      | Très Bien      |
| 14 – 15.9 | Bien           |
| 12 – 13.9 | Assez Bien     |
| 10 – 11.9 | Passable       |
| < 10      | Insuffisant    |

## Idées d'améliorations

- Sauvegarde persistante (fichier JSON / base de données SQLite)
- Interface graphique avec Tkinter ou PyQt
- Export PDF des bulletins
- Application web avec Flask ou Django
