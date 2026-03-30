<?php

namespace App\Entity;

use App\Repository\EtudiantRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity(repositoryClass: EtudiantRepository::class)]
#[ORM\Table(name: 'etudiant')]
class Etudiant
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 100)]
    #[Assert\NotBlank(message: 'Le nom ne peut pas être vide.')]
    #[Assert\Length(min: 2, max: 100)]
    private ?string $nom = null;

    #[ORM\Column(length: 100)]
    #[Assert\NotBlank(message: 'Le prénom ne peut pas être vide.')]
    #[Assert\Length(min: 2, max: 100)]
    private ?string $prenom = null;

    #[ORM\Column(length: 20, unique: true)]
    #[Assert\NotBlank(message: 'Le numéro étudiant ne peut pas être vide.')]
    private ?string $numeroEtudiant = null;

    #[ORM\Column(length: 255)]
    #[Assert\NotBlank(message: 'L\'email ne peut pas être vide.')]
    #[Assert\Email(message: 'L\'email {{ value }} n\'est pas valide.')]
    private ?string $email = null;

    #[ORM\Column(type: 'date')]
    #[Assert\NotNull(message: 'La date de naissance est requise.')]
    private ?\DateTimeInterface $dateNaissance = null;

    #[ORM\Column(length: 50)]
    #[Assert\NotBlank]
    #[Assert\Choice(choices: ['L1', 'L2', 'L3', 'M1', 'M2'], message: 'Niveau invalide.')]
    private ?string $niveau = null;

    #[ORM\OneToMany(mappedBy: 'etudiant', targetEntity: Note::class, cascade: ['persist', 'remove'])]
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

    public function getPrenom(): ?string
    {
        return $this->prenom;
    }

    public function setPrenom(string $prenom): static
    {
        $this->prenom = $prenom;
        return $this;
    }

    public function getNumeroEtudiant(): ?string
    {
        return $this->numeroEtudiant;
    }

    public function setNumeroEtudiant(string $numeroEtudiant): static
    {
        $this->numeroEtudiant = $numeroEtudiant;
        return $this;
    }

    public function getEmail(): ?string
    {
        return $this->email;
    }

    public function setEmail(string $email): static
    {
        $this->email = $email;
        return $this;
    }

    public function getDateNaissance(): ?\DateTimeInterface
    {
        return $this->dateNaissance;
    }

    public function setDateNaissance(\DateTimeInterface $dateNaissance): static
    {
        $this->dateNaissance = $dateNaissance;
        return $this;
    }

    public function getNiveau(): ?string
    {
        return $this->niveau;
    }

    public function setNiveau(string $niveau): static
    {
        $this->niveau = $niveau;
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
            $note->setEtudiant($this);
        }
        return $this;
    }

    public function removeNote(Note $note): static
    {
        if ($this->notes->removeElement($note)) {
            if ($note->getEtudiant() === $this) {
                $note->setEtudiant(null);
            }
        }
        return $this;
    }

    /**
     * Calcule la moyenne générale de l'étudiant.
     */
    public function getMoyenneGenerale(): float
    {
        if ($this->notes->isEmpty()) {
            return 0.0;
        }

        $totalPoints = 0.0;
        $totalCoefficients = 0.0;

        foreach ($this->notes as $note) {
            $coefficient = $note->getMatiere()->getCoefficient();
            $totalPoints += $note->getValeur() * $coefficient;
            $totalCoefficients += $coefficient;
        }

        if ($totalCoefficients === 0.0) {
            return 0.0;
        }

        return round($totalPoints / $totalCoefficients, 2);
    }

    /**
     * Détermine si l'étudiant est admis (moyenne >= 10).
     */
    public function isAdmis(): bool
    {
        return $this->getMoyenneGenerale() >= 10.0;
    }

    public function getNomComplet(): string
    {
        return $this->prenom . ' ' . $this->nom;
    }

    public function __toString(): string
    {
        return $this->getNomComplet();
    }
}
