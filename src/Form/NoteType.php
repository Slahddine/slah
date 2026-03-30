<?php

namespace App\Form;

use App\Entity\Etudiant;
use App\Entity\Matiere;
use App\Entity\Note;
use Symfony\Bridge\Doctrine\Form\Type\EntityType;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\NumberType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class NoteType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('valeur', NumberType::class, [
                'label' => 'Note (0-20)',
                'attr' => [
                    'placeholder' => 'Ex: 14.5',
                    'class' => 'form-control',
                    'min' => 0,
                    'max' => 20,
                    'step' => 0.25,
                ],
            ])
            ->add('typeEvaluation', ChoiceType::class, [
                'label' => 'Type d\'Évaluation',
                'choices' => [
                    'Contrôle Continu' => 'CC',
                    'Examen' => 'Examen',
                    'Travaux Pratiques' => 'TP',
                    'Rattrapage' => 'Rattrapage',
                ],
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
            ->add('dateEvaluation', DateType::class, [
                'label' => 'Date de l\'Évaluation',
                'widget' => 'single_text',
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
            ->add('etudiant', EntityType::class, [
                'class' => Etudiant::class,
                'label' => 'Étudiant',
                'choice_label' => 'nomComplet',
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
            ->add('matiere', EntityType::class, [
                'class' => Matiere::class,
                'label' => 'Matière',
                'choice_label' => function (Matiere $matiere) {
                    return $matiere->getNom() . ' (' . $matiere->getCode() . ')';
                },
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
        ;
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Note::class,
        ]);
    }
}
