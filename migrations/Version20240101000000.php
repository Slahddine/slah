<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Migration initiale — création des tables etudiant, matiere et note.
 */
final class Version20240101000000 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Création des tables etudiant, matiere et note';
    }

    public function up(Schema $schema): void
    {
        // Table etudiant
        $this->addSql('CREATE TABLE etudiant (
            id INT AUTO_INCREMENT NOT NULL,
            nom VARCHAR(100) NOT NULL,
            prenom VARCHAR(100) NOT NULL,
            numero_etudiant VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL,
            date_naissance DATE NOT NULL,
            niveau VARCHAR(50) NOT NULL,
            UNIQUE INDEX UNIQ_717E1EB6E20AE157 (numero_etudiant),
            PRIMARY KEY(id)
        ) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');

        // Table matiere
        $this->addSql('CREATE TABLE matiere (
            id INT AUTO_INCREMENT NOT NULL,
            nom VARCHAR(150) NOT NULL,
            code VARCHAR(20) NOT NULL,
            coefficient DOUBLE PRECISION NOT NULL,
            volume_horaire INT NOT NULL,
            semestre VARCHAR(50) NOT NULL,
            PRIMARY KEY(id)
        ) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');

        // Table note
        $this->addSql('CREATE TABLE note (
            id INT AUTO_INCREMENT NOT NULL,
            etudiant_id INT NOT NULL,
            matiere_id INT NOT NULL,
            valeur DOUBLE PRECISION NOT NULL,
            type_evaluation VARCHAR(20) NOT NULL,
            date_evaluation DATE NOT NULL,
            INDEX IDX_CFBDFA14DDEAB1A3 (etudiant_id),
            INDEX IDX_CFBDFA14F46CD258 (matiere_id),
            PRIMARY KEY(id)
        ) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');

        // Clés étrangères
        $this->addSql('ALTER TABLE note
            ADD CONSTRAINT FK_CFBDFA14DDEAB1A3 FOREIGN KEY (etudiant_id) REFERENCES etudiant (id),
            ADD CONSTRAINT FK_CFBDFA14F46CD258 FOREIGN KEY (matiere_id) REFERENCES matiere (id)
        ');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE note DROP FOREIGN KEY FK_CFBDFA14DDEAB1A3');
        $this->addSql('ALTER TABLE note DROP FOREIGN KEY FK_CFBDFA14F46CD258');
        $this->addSql('DROP TABLE note');
        $this->addSql('DROP TABLE matiere');
        $this->addSql('DROP TABLE etudiant');
    }
}
