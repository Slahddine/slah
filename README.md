# Système de Gestion des Notes Étudiantes

**Projet Informatique — Python**

Un système en ligne de commande permettant de gérer les notes des étudiants : ajout d'étudiants, saisie de notes par matière, calcul de moyennes, classement et mention.

---

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| Ajouter un étudiant | Enregistrer un étudiant avec son nom et son numéro |
| Saisir une note | Ajouter une note (0–20) pour une matière donnée |
| Afficher les notes | Voir les notes et la moyenne d'un étudiant |
| Classement | Lister tous les étudiants par ordre de moyenne décroissante |
| Moyenne de classe | Calculer la moyenne générale de la classe |
| Meilleur étudiant | Identifier l'étudiant ayant la meilleure moyenne |
| Supprimer un étudiant | Retirer un étudiant du carnet de notes |

Les données sont sauvegardées automatiquement dans le fichier `gradebook.json`.

---

## Structure du projet

```
.
├── grades.py        # Logique métier : classes Student et GradeBook
├── main.py          # Interface en ligne de commande
├── test_grades.py   # Tests unitaires (pytest)
└── gradebook.json   # Données (créé automatiquement)
```

---

## Prérequis

- Python 3.10 ou supérieur

---

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/Slahddine/slah.git
cd slah

# (Optionnel) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate
```

---

## Utilisation

```bash
python main.py
```

Exemple de session :

```
=============================================
  Système de Gestion des Notes Étudiantes
=============================================
  1. Ajouter un étudiant
  2. Saisir une note
  3. Afficher les notes d'un étudiant
  4. Afficher le classement de la classe
  5. Moyenne générale de la classe
  6. Meilleur étudiant
  7. Supprimer un étudiant
  0. Quitter
=============================================
Votre choix : 1
Nom de l'étudiant : Slah
Numéro étudiant   : S001
✓ Étudiant 'Slah' ajouté avec succès.
```

---

## Tests

```bash
python -m pytest test_grades.py -v
```

---

## Barème des mentions

| Moyenne | Mention |
|---|---|
| 16 – 20 | Très Bien |
| 14 – 15.99 | Bien |
| 12 – 13.99 | Assez Bien |
| 10 – 11.99 | Passable |
| 0 – 9.99 | Insuffisant |
