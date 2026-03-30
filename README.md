# TP Symfony — Gestion des Étudiants

Application Symfony 6 permettant de gérer les **étudiants**, les **matières** et les **notes** d'une université.

## Fonctionnalités

| Module | Opérations |
|--------|-----------|
| **Étudiants** | Créer · Lire · Modifier · Supprimer · Rechercher · Filtrer par niveau |
| **Matières** | Créer · Lire · Modifier · Supprimer · Filtrer par semestre |
| **Notes** | Saisir · Consulter · Modifier · Supprimer |
| **Statistiques** | Moyenne générale (pondérée) · Mention · Statut admis/ajourné |

## Structure du projet

```
src/
├── Controller/
│   ├── HomeController.php        # Page d'accueil
│   ├── EtudiantController.php    # CRUD étudiants
│   ├── MatiereController.php     # CRUD matières
│   └── NoteController.php        # CRUD notes
├── Entity/
│   ├── Etudiant.php              # Entité étudiant (avec calcul de moyenne)
│   ├── Matiere.php               # Entité matière
│   └── Note.php                  # Entité note (avec mention)
├── Form/
│   ├── EtudiantType.php          # Formulaire étudiant
│   ├── MatiereType.php           # Formulaire matière
│   └── NoteType.php              # Formulaire note
└── Repository/
    ├── EtudiantRepository.php    # Requêtes personnalisées étudiants
    ├── MatiereRepository.php     # Requêtes personnalisées matières
    └── NoteRepository.php        # Requêtes personnalisées notes

templates/
├── base.html.twig                # Layout Bootstrap 5
├── home/index.html.twig          # Accueil
├── etudiant/                     # Templates CRUD étudiants
├── matiere/                      # Templates CRUD matières
└── note/                         # Templates CRUD notes

migrations/
└── Version20240101000000.php     # Migration initiale (tables SQL)
```

## Installation

### Prérequis

- PHP 8.1+
- Composer
- MySQL / MariaDB

### Étapes

```bash
# 1. Installer les dépendances
composer install

# 2. Configurer la base de données dans .env
DATABASE_URL="mysql://utilisateur:motdepasse@127.0.0.1:3306/tp_symfony?serverVersion=8.0"

# 3. Créer la base de données
php bin/console doctrine:database:create

# 4. Appliquer les migrations
php bin/console doctrine:migrations:migrate

# 5. Lancer le serveur de développement
symfony server:start
# ou
php -S localhost:8000 -t public/
```

## Entités et relations

```
Etudiant  ----< Note >----  Matiere
(1)                          (1)
```

- Un **Etudiant** peut avoir plusieurs **Notes**.
- Une **Matiere** peut avoir plusieurs **Notes**.
- Une **Note** appartient à exactement un **Etudiant** et une **Matiere**.

## Calcul de la moyenne

La moyenne générale d'un étudiant est **pondérée par les coefficients** des matières :

```
Moyenne = Σ(note × coefficient) / Σ(coefficients)
```

Un étudiant est **admis** si sa moyenne générale est ≥ 10/20.

## Mentions

| Note | Mention |
|------|---------|
| ≥ 16 | Très Bien |
| ≥ 14 | Bien |
| ≥ 12 | Assez Bien |
| ≥ 10 | Passable |
| < 10 | Insuffisant |
