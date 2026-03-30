<?php

namespace App\Repository;

use App\Entity\Matiere;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @extends ServiceEntityRepository<Matiere>
 *
 * @method Matiere|null find($id, $lockMode = null, $lockVersion = null)
 * @method Matiere|null findOneBy(array $criteria, array $orderBy = null)
 * @method Matiere[]    findAll()
 * @method Matiere[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class MatiereRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Matiere::class);
    }

    /**
     * Récupère les matières par semestre.
     *
     * @return Matiere[]
     */
    public function findBySemestre(string $semestre): array
    {
        return $this->createQueryBuilder('m')
            ->andWhere('m.semestre = :semestre')
            ->setParameter('semestre', $semestre)
            ->orderBy('m.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Recherche des matières par nom ou code.
     *
     * @return Matiere[]
     */
    public function findByNomOuCode(string $terme): array
    {
        return $this->createQueryBuilder('m')
            ->andWhere('m.nom LIKE :terme OR m.code LIKE :terme')
            ->setParameter('terme', '%' . $terme . '%')
            ->orderBy('m.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    /**
     * Récupère les matières avec leurs notes.
     *
     * @return Matiere[]
     */
    public function findAllWithNotes(): array
    {
        return $this->createQueryBuilder('m')
            ->leftJoin('m.notes', 'n')
            ->addSelect('n')
            ->orderBy('m.semestre', 'ASC')
            ->addOrderBy('m.nom', 'ASC')
            ->getQuery()
            ->getResult();
    }

    public function save(Matiere $entity, bool $flush = false): void
    {
        $this->getEntityManager()->persist($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }

    public function remove(Matiere $entity, bool $flush = false): void
    {
        $this->getEntityManager()->remove($entity);

        if ($flush) {
            $this->getEntityManager()->flush();
        }
    }
}
