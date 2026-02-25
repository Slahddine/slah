# Système de Gestion des Notes Étudiants

Un projet informatique en Python pour gérer les notes des étudiants, calculer les moyennes et déterminer les résultats (admis / ajourné).

## Fonctionnalités

- ➕ Ajouter / supprimer des étudiants
- 📝 Enregistrer des notes par matière (sur 20)
- 📊 Calculer la moyenne, le minimum et le maximum
- ✅ Afficher le statut : **Admis** (moyenne ≥ 10) ou **Ajourné**
- 💾 Sauvegarde automatique dans un fichier JSON (`students.json`)

## Structure du projet

```
├── grades.py        # Module principal (logique métier)
├── main.py          # Interface en ligne de commande (CLI)
├── test_grades.py   # Tests unitaires
└── students.json    # Données (créé automatiquement)
```

## Lancer l'application

```bash
python main.py
```

### Menu principal

```
===== Gestion des Notes =====
1. Ajouter un étudiant
2. Supprimer un étudiant
3. Ajouter une note
4. Voir les résultats d'un étudiant
5. Liste des étudiants
0. Quitter
```

## Exemple d'utilisation

```
Votre choix: 1
Nom de l'étudiant: Salah
→ Étudiant 'Salah' ajouté avec succès.

Votre choix: 3
Nom de l'étudiant: Salah
Matière: Mathématiques
Note (0-20): 14
→ Note 14.0/20 en 'Mathématiques' ajoutée pour 'Salah'.

Votre choix: 4
Nom de l'étudiant: Salah

--- Résultats de Salah ---
  Mathématiques: 14.0/20
  Moyenne : 14.0/20
  Min : 14.0 | Max : 14.0
  Statut  : Admis
```

## Lancer les tests

```bash
python -m unittest test_grades -v
```

## Technologies utilisées

- Python 3 (stdlib uniquement — pas de dépendances externes)
- JSON pour la persistance des données
- `unittest` pour les tests

## Idées d'améliorations futures

- Interface graphique (Tkinter ou web avec Flask)
- Export PDF des bulletins
- Authentification (admin / étudiant)
- Base de données SQLite
