# 📚 Gestionnaire de Notes Étudiantes

Un projet informatique en Python pour gérer les notes des étudiants, calculer les moyennes et afficher les mentions académiques.

## Fonctionnalités

- ✅ Ajouter des étudiants
- ✅ Enregistrer des notes (sur 20)
- ✅ Calculer la moyenne de chaque étudiant
- ✅ Afficher la mention (Très Bien, Bien, Assez Bien, Passable, Insuffisant)
- ✅ Classement de la classe
- ✅ Interface en ligne de commande interactive

## Structure du projet

```
slah/
├── grades.py         # Logique métier (calculs, gestion des données)
├── main.py           # Interface utilisateur (CLI)
├── test_grades.py    # Tests unitaires
├── requirements.txt  # Dépendances
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

Exemple de session :

```
----------------------------------------
  Gestionnaire de Notes Étudiantes
----------------------------------------
1. Ajouter un étudiant
2. Ajouter une note
3. Voir le bulletin d'un étudiant
4. Classement de la classe
5. Liste des étudiants
0. Quitter
----------------------------------------
Votre choix : 1
Nom de l'étudiant : Alice
✓ Étudiant 'Alice' ajouté.
...
Votre choix : 3
Nom de l'étudiant : Alice
----------------------------------------
  Bulletin de Alice
----------------------------------------
  Notes    : [14, 16, 18]
  Moyenne  : 16.00/20
  Mention  : Très Bien
----------------------------------------
```

## Tests

```bash
pytest test_grades.py -v
```

## Barème des mentions

| Moyenne       | Mention       |
|---------------|---------------|
| 16 – 20       | Très Bien     |
| 14 – 15.99    | Bien          |
| 12 – 13.99    | Assez Bien    |
| 10 – 11.99    | Passable      |
| < 10          | Insuffisant   |
