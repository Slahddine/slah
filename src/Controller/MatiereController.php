<?php

namespace App\Controller;

use App\Entity\Matiere;
use App\Form\MatiereType;
use App\Repository\MatiereRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/matiere')]
class MatiereController extends AbstractController
{
    #[Route('/', name: 'app_matiere_index', methods: ['GET'])]
    public function index(Request $request, MatiereRepository $matiereRepository): Response
    {
        $semestre = $request->query->get('semestre');
        $terme = $request->query->get('recherche');

        if ($terme) {
            $matieres = $matiereRepository->findByNomOuCode($terme);
        } elseif ($semestre) {
            $matieres = $matiereRepository->findBySemestre($semestre);
        } else {
            $matieres = $matiereRepository->findBy([], ['semestre' => 'ASC', 'nom' => 'ASC']);
        }

        return $this->render('matiere/index.html.twig', [
            'matieres' => $matieres,
            'semestre' => $semestre,
            'terme' => $terme,
        ]);
    }

    #[Route('/nouvelle', name: 'app_matiere_new', methods: ['GET', 'POST'])]
    public function new(Request $request, EntityManagerInterface $entityManager): Response
    {
        $matiere = new Matiere();
        $form = $this->createForm(MatiereType::class, $matiere);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->persist($matiere);
            $entityManager->flush();

            $this->addFlash('success', 'La matière a été ajoutée avec succès.');

            return $this->redirectToRoute('app_matiere_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->render('matiere/new.html.twig', [
            'matiere' => $matiere,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_matiere_show', methods: ['GET'])]
    public function show(Matiere $matiere): Response
    {
        return $this->render('matiere/show.html.twig', [
            'matiere' => $matiere,
        ]);
    }

    #[Route('/{id}/modifier', name: 'app_matiere_edit', methods: ['GET', 'POST'])]
    public function edit(Request $request, Matiere $matiere, EntityManagerInterface $entityManager): Response
    {
        $form = $this->createForm(MatiereType::class, $matiere);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->flush();

            $this->addFlash('success', 'La matière a été modifiée avec succès.');

            return $this->redirectToRoute('app_matiere_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->render('matiere/edit.html.twig', [
            'matiere' => $matiere,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_matiere_delete', methods: ['POST'])]
    public function delete(Request $request, Matiere $matiere, EntityManagerInterface $entityManager): Response
    {
        if ($this->isCsrfTokenValid('delete' . $matiere->getId(), $request->request->get('_token'))) {
            $entityManager->remove($matiere);
            $entityManager->flush();

            $this->addFlash('success', 'La matière a été supprimée avec succès.');
        }

        return $this->redirectToRoute('app_matiere_index', [], Response::HTTP_SEE_OTHER);
    }
}
