<?php

namespace App\Entity;

use App\Repository\ArticleRepository;
use Doctrine\Common\Collections\ArrayCollection;
use Doctrine\Common\Collections\Collection;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=ArticleRepository::class)
 */
class Article
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $soustitle;

    /**
     * @ORM\OneToMany(targetEntity=Commmentaire::class, mappedBy="article")
     */
    private $commmentaires;

    public function __construct()
    {
        $this->commmentaires = new ArrayCollection();
    }

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getSoustitle(): ?string
    {
        return $this->soustitle;
    }

    public function setSoustitle(string $soustitle): self
    {
        $this->soustitle = $soustitle;

        return $this;
    }

    /**
     * @return Collection<int, Commmentaire>
     */
    public function getCommmentaires(): Collection
    {
        return $this->commmentaires;
    }

    public function addCommmentaire(Commmentaire $commmentaire): self
    {
        if (!$this->commmentaires->contains($commmentaire)) {
            $this->commmentaires[] = $commmentaire;
            $commmentaire->setArticle($this);
        }

        return $this;
    }

    public function removeCommmentaire(Commmentaire $commmentaire): self
    {
        if ($this->commmentaires->removeElement($commmentaire)) {
            // set the owning side to null (unless already changed)
            if ($commmentaire->getArticle() === $this) {
                $commmentaire->setArticle(null);
            }
        }

        return $this;
    }
}
