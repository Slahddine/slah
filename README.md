# Système de Gestion des Notes 📚

A simple command-line **Student Grade Management System** written in Python.

## Features

- Add and remove students
- Record grades per subject (out of 20)
- Calculate averages with mention (Très Bien, Bien, Assez Bien, Passable, Insuffisant)
- Display a ranked leaderboard of all students
- Persistent storage via a local JSON file (`students.json`)

## Requirements

- Python 3.6+

## Usage

```bash
python grades.py
```

### Menu options

| Option | Description |
|--------|-------------|
| 1 | Add a student |
| 2 | Add a grade for a student |
| 3 | Show grades and average for a student |
| 4 | Show full class ranking |
| 5 | Remove a student |
| 0 | Quit |

## Example session

```
=== Système de Gestion des Notes ===

Menu:
  1. Ajouter un étudiant
  ...
  4. Afficher le classement

=== Classement des étudiants ===
  1. Slah: 16.50/20 (Très Bien)
  2. Ahmed: 13.00/20 (Assez Bien)
  3. Sara: 9.50/20 (Insuffisant)
```

## Grading scale

| Average | Mention |
|---------|---------|
| ≥ 16    | Très Bien |
| ≥ 14    | Bien |
| ≥ 12    | Assez Bien |
| ≥ 10    | Passable |
| < 10    | Insuffisant |
