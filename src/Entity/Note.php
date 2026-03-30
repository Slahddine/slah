<?php

namespace App\Entity;

use App\Repository\NoteRepository;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity(repositoryClass: NoteRepository::class)]
#[ORM\Table(name: 'note')]
class Note
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(type: 'float')]
    #[Assert\NotNull(message: 'La valeur de la note est requise.')]
    #[Assert\Range(
        min: 0,
        max: 20,
        notInRangeMessage: 'La note doit être entre {{ min }} et {{ max }}.'
    )]
    private ?float $valeur = null;

    #[ORM\Column(length: 20)]
    #[Assert\NotBlank]
    #[Assert\Choice(choices: ['CC', 'Examen', 'TP', 'Rattrapage'], message: 'Type de note invalide.')]
    private ?string $typeEvaluation = null;

    #[ORM\Column(type: 'date')]
    #[Assert\NotNull(message: 'La date de l\'évaluation est requise.')]
    private ?\DateTimeInterface $dateEvaluation = null;

    #[ORM\ManyToOne(inversedBy: 'notes')]
    #[ORM\JoinColumn(nullable: false)]
    #[Assert\NotNull(message: 'L\'étudiant est requis.')]
    private ?Etudiant $etudiant = null;

    #[ORM\ManyToOne(inversedBy: 'notes')]
    #[ORM\JoinColumn(nullable: false)]
    #[Assert\NotNull(message: 'La matière est requise.')]
    private ?Matiere $matiere = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getValeur(): ?float
    {
        return $this->valeur;
    }

    public function setValeur(float $valeur): static
    {
        $this->valeur = $valeur;
        return $this;
    }

    public function getTypeEvaluation(): ?string
    {
        return $this->typeEvaluation;
    }

    public function setTypeEvaluation(string $typeEvaluation): static
    {
        $this->typeEvaluation = $typeEvaluation;
        return $this;
    }

    public function getDateEvaluation(): ?\DateTimeInterface
    {
        return $this->dateEvaluation;
    }

    public function setDateEvaluation(\DateTimeInterface $dateEvaluation): static
    {
        $this->dateEvaluation = $dateEvaluation;
        return $this;
    }

    public function getEtudiant(): ?Etudiant
    {
        return $this->etudiant;
    }

    public function setEtudiant(?Etudiant $etudiant): static
    {
        $this->etudiant = $etudiant;
        return $this;
    }

    public function getMatiere(): ?Matiere
    {
        return $this->matiere;
    }

    public function setMatiere(?Matiere $matiere): static
    {
        $this->matiere = $matiere;
        return $this;
    }

    /**
     * Détermine si la note est une note de passage (>= 10).
     */
    public function isPassante(): bool
    {
        return $this->valeur >= 10.0;
    }

    /**
     * Retourne la mention selon la note.
     */
    public function getMention(): string
    {
        return match (true) {
            $this->valeur >= 16 => 'Très Bien',
            $this->valeur >= 14 => 'Bien',
            $this->valeur >= 12 => 'Assez Bien',
            $this->valeur >= 10 => 'Passable',
            default => 'Insuffisant',
        };
    }

    public function __toString(): string
    {
        return sprintf(
            '%s - %s: %s/20',
            $this->etudiant?->getNomComplet(),
            $this->matiere?->getNom(),
            $this->valeur
        );
    }
}
