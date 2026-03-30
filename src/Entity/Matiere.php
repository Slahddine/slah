<?php

namespace App\Entity;

use App\Repository\MatiereRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity(repositoryClass: MatiereRepository::class)]
#[ORM\Table(name: 'matiere')]
class Matiere
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 150)]
    #[Assert\NotBlank(message: 'Le nom de la matière ne peut pas être vide.')]
    #[Assert\Length(min: 2, max: 150)]
    private ?string $nom = null;

    #[ORM\Column(length: 20)]
    #[Assert\NotBlank(message: 'Le code de la matière est requis.')]
    private ?string $code = null;

    #[ORM\Column(type: 'float')]
    #[Assert\NotNull]
    #[Assert\Positive(message: 'Le coefficient doit être positif.')]
    #[Assert\LessThanOrEqual(value: 10, message: 'Le coefficient ne peut pas dépasser 10.')]
    private ?float $coefficient = null;

    #[ORM\Column(type: 'integer')]
    #[Assert\NotNull]
    #[Assert\Positive(message: 'Le volume horaire doit être positif.')]
    private ?int $volumeHoraire = null;

    #[ORM\Column(length: 50)]
    #[Assert\NotBlank]
    #[Assert\Choice(choices: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'], message: 'Semestre invalide.')]
    private ?string $semestre = null;

    #[ORM\OneToMany(mappedBy: 'matiere', targetEntity: Note::class, cascade: ['persist', 'remove'])]
    private Collection $notes;

    public function __construct()
    {
        $this->notes = new ArrayCollection();
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getNom(): ?string
    {
        return $this->nom;
    }

    public function setNom(string $nom): static
    {
        $this->nom = $nom;
        return $this;
    }

    public function getCode(): ?string
    {
        return $this->code;
    }

    public function setCode(string $code): static
    {
        $this->code = $code;
        return $this;
    }

    public function getCoefficient(): ?float
    {
        return $this->coefficient;
    }

    public function setCoefficient(float $coefficient): static
    {
        $this->coefficient = $coefficient;
        return $this;
    }

    public function getVolumeHoraire(): ?int
    {
        return $this->volumeHoraire;
    }

    public function setVolumeHoraire(int $volumeHoraire): static
    {
        $this->volumeHoraire = $volumeHoraire;
        return $this;
    }

    public function getSemestre(): ?string
    {
        return $this->semestre;
    }

    public function setSemestre(string $semestre): static
    {
        $this->semestre = $semestre;
        return $this;
    }

    /**
     * @return Collection<int, Note>
     */
    public function getNotes(): Collection
    {
        return $this->notes;
    }

    public function addNote(Note $note): static
    {
        if (!$this->notes->contains($note)) {
            $this->notes->add($note);
            $note->setMatiere($this);
        }
        return $this;
    }

    public function removeNote(Note $note): static
    {
        if ($this->notes->removeElement($note)) {
            if ($note->getMatiere() === $this) {
                $note->setMatiere(null);
            }
        }
        return $this;
    }

    /**
     * Calcule la moyenne de la matière.
     */
    public function getMoyenne(): float
    {
        if ($this->notes->isEmpty()) {
            return 0.0;
        }

        $total = 0.0;
        foreach ($this->notes as $note) {
            $total += $note->getValeur();
        }

        return round($total / count($this->notes), 2);
    }

    public function __toString(): string
    {
        return $this->nom . ' (' . $this->code . ')';
    }
}
