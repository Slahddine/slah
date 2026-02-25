# Système de Gestion des Notes Étudiants 🎓

Un projet Python simple et complet pour gérer les notes des étudiants — idéal comme **projet informatique**.

## Fonctionnalités

- Ajouter / supprimer des étudiants
- Enregistrer les notes par matière (sur 20)
- Calculer la moyenne générale d'un étudiant
- Attribuer automatiquement une mention (Très Bien, Bien, Assez Bien, Passable, Insuffisant)
- Déterminer si l'étudiant est **Admis** ou **Ajourné** (seuil : 10/20)
- Afficher un bulletin de notes individuel
- Voir la moyenne de classe, le major de promotion, et le nombre d'admis/ajournés

## Structure du projet

```
slah/
├── grades.py            # Module principal (Student + GradeBook)
├── tests/
│   └── test_grades.py   # Tests unitaires (pytest)
└── README.md
```

## Utilisation rapide

```python
from grades import GradeBook

book = GradeBook()

# Ajouter des étudiants
ali   = book.add_student("Ali Ben Salah", "S001")
sarra = book.add_student("Sarra Trabelsi", "S002")

# Enregistrer les notes
ali.add_grade("Mathématiques", 15)
ali.add_grade("Informatique", 17)
ali.add_grade("Physique", 13)

sarra.add_grade("Mathématiques", 9)
sarra.add_grade("Informatique", 11)
sarra.add_grade("Physique", 8)

# Bulletin individuel
print(ali.report())
# ----------------------------------------
# Étudiant : Ali Ben Salah (ID: S001)
# ----------------------------------------
#   Mathématiques        : 15.00/20
#   Informatique         : 17.00/20
#   Physique             : 13.00/20
# ----------------------------------------
#   Moyenne               : 15.00/20
#   Mention               : Bien
#   Résultat              : Admis

# Récapitulatif de classe
print(book.summary())
```

## Lancer les tests

```bash
pip install pytest
pytest tests/ -v
```

## Barème des mentions

| Moyenne       | Mention        |
|---------------|----------------|
| ≥ 16          | Très Bien      |
| 14 – 15.99    | Bien           |
| 12 – 13.99    | Assez Bien     |
| 10 – 11.99    | Passable       |
| < 10          | Insuffisant    |
