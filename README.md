# 📚 Gestionnaire de Notes — Student Grade Management System

Un projet web simple et pratique pour gérer les notes des étudiants. Idéal comme projet informatique scolaire ou universitaire.

## 🎯 Fonctionnalités

- ➕ **Ajouter des étudiants** avec leurs notes dans 4 matières (Maths, Physique, Français, Sciences)
- 📊 **Calcul automatique** de la moyenne par étudiant
- ✅ **Résultat automatique** : Admis (≥ 10/20) ou Recalé (< 10/20)
- 📈 **Statistiques de classe** : nombre d'admis, recalés, et moyenne générale
- 💾 **Sauvegarde locale** (localStorage) — les données persistent après le rechargement de la page
- 🗑️ **Suppression** individuelle ou totale des enregistrements

## 🛠️ Technologies utilisées

| Technologie | Rôle |
|---|---|
| HTML5 | Structure de la page |
| CSS3 | Mise en forme et responsive design |
| JavaScript (ES6+) | Logique applicative |
| localStorage | Persistance des données côté client |

## 🚀 Lancement

Aucune installation requise. Ouvrez simplement `index.html` dans votre navigateur :

```bash
# Avec Python (serveur local optionnel)
python -m http.server 8000
# Puis ouvrez http://localhost:8000
```

Ou double-cliquez directement sur le fichier `index.html`.

## 📁 Structure du projet

```
slah/
├── index.html   # Interface principale
├── style.css    # Feuille de style
├── app.js       # Logique JavaScript
└── README.md    # Documentation
```

## 📷 Aperçu

| Section | Description |
|---|---|
| Formulaire | Saisie du nom et des 4 notes |
| Statistiques | Résumé de la classe (total, admis, recalés, moyenne) |
| Tableau | Liste complète avec résultat par étudiant |

## 💡 Idées d'améliorations

- Exporter les résultats en PDF ou Excel
- Ajouter des matières personnalisées avec coefficients
- Authentification enseignant / élève
- Graphiques de progression (Chart.js)
- Support multi-classes
