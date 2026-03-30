<?php

namespace App\Repository;

use App\Entity\Etudiant;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Etudiant>
 *
 * @method Etudiant|null find($id, $lockMode = null, $lockVersion = null)
 * @method Etudiant|null findOneBy(array $criteria, array $orderBy = null)
 * @method Etudiant[]    findAll()
 * @method Etudiant[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class EtudiantRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Etudiant::class);
    }

    /**
     * Recherche des étudiants par nom ou prénom.
     *
     * @return Etudiant[]
     */
    public function findByNomOuPrenom(string $terme): array
    {
        return $this->createQueryBuilder('e')
            ->andWhere('e.nom LIKE :terme OR e.prenom LIKE :terme OR e.numeroEtudiant LIKE :terme')
            ->setParameter('terme', '%' . $terme . '%')
            ->orderBy('e.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Recherche des étudiants par niveau.
     *
     * @return Etudiant[]
     */
    public function findByNiveau(string $niveau): array
    {
        return $this->createQueryBuilder('e')
            ->andWhere('e.niveau = :niveau')
            ->setParameter('niveau', $niveau)
            ->orderBy('e.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Récupère les étudiants avec leurs notes (jointure).
     *
     * @return Etudiant[]
     */
    public function findAllWithNotes(): array
    {
        return $this->createQueryBuilder('e')
            ->leftJoin('e.notes', 'n')
            ->leftJoin('n.matiere', 'm')
            ->addSelect('n', 'm')
            ->orderBy('e.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Compte le nombre d'étudiants par niveau.
     */
    public function countByNiveau(): array
    {
        return $this->createQueryBuilder('e')
            ->select('e.niveau, COUNT(e.id) as total')
            ->groupBy('e.niveau')
            ->getQuery()
            ->getResult();
    }

    public function save(Etudiant $entity, bool $flush = false): void
    {
        $this->getEntityManager()->persist($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }

    public function remove(Etudiant $entity, bool $flush = false): void
    {
        $this->getEntityManager()->remove($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }
}
