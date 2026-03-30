<?php

namespace App\Repository;

use App\Entity\Etudiant;
use App\Entity\Matiere;
use App\Entity\Note;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Note>
 *
 * @method Note|null find($id, $lockMode = null, $lockVersion = null)
 * @method Note|null findOneBy(array $criteria, array $orderBy = null)
 * @method Note[]    findAll()
 * @method Note[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class NoteRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Note::class);
    }

    /**
     * Récupère les notes d'un étudiant.
     *
     * @return Note[]
     */
    public function findByEtudiant(Etudiant $etudiant): array
    {
        return $this->createQueryBuilder('n')
            ->andWhere('n.etudiant = :etudiant')
            ->setParameter('etudiant', $etudiant)
            ->leftJoin('n.matiere', 'm')
            ->addSelect('m')
            ->orderBy('m.semestre', 'ASC')
            ->addOrderBy('m.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Récupère les notes d'une matière.
     *
     * @return Note[]
     */
    public function findByMatiere(Matiere $matiere): array
    {
        return $this->createQueryBuilder('n')
            ->andWhere('n.matiere = :matiere')
            ->setParameter('matiere', $matiere)
            ->leftJoin('n.etudiant', 'e')
            ->addSelect('e')
            ->orderBy('n.valeur', 'DESC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Calcule la moyenne d'une matière.
     */
    public function getMoyenneParMatiere(Matiere $matiere): float
    {
        $result = $this->createQueryBuilder('n')
            ->select('AVG(n.valeur) as moyenne')
            ->andWhere('n.matiere = :matiere')
            ->setParameter('matiere', $matiere)
            ->getQuery()
            ->getSingleScalarResult();

        return round((float) $result, 2);
    }

    /**
     * Récupère les notes avec toutes les relations chargées.
     *
     * @return Note[]
     */
    public function findAllWithRelations(): array
    {
        return $this->createQueryBuilder('n')
            ->leftJoin('n.etudiant', 'e')
            ->leftJoin('n.matiere', 'm')
            ->addSelect('e', 'm')
            ->orderBy('e.nom', 'ASC')
            ->addOrderBy('m.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Récupère les notes d'un étudiant pour une matière donnée.
     *
     * @return Note[]
     */
    public function findByEtudiantAndMatiere(Etudiant $etudiant, Matiere $matiere): array
    {
        return $this->createQueryBuilder('n')
            ->andWhere('n.etudiant = :etudiant')
            ->andWhere('n.matiere = :matiere')
            ->setParameter('etudiant', $etudiant)
            ->setParameter('matiere', $matiere)
            ->orderBy('n.dateEvaluation', 'DESC')
            ->getQuery()
            ->getResult();
    }

    public function save(Note $entity, bool $flush = false): void
    {
        $this->getEntityManager()->persist($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }

    public function remove(Note $entity, bool $flush = false): void
    {
        $this->getEntityManager()->remove($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }
}
