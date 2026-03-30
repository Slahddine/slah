<?php

namespace App\Form;

use App\Entity\Matiere;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Component\Form\Extension\Core\Type\IntegerType;
use Symfony\Component\Form\Extension\Core\Type\NumberType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class MatiereType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('nom', TextType::class, [
                'label' => 'Nom de la Matière',
                'attr' => [
                    'placeholder' => 'Ex: Mathématiques',
                    'class' => 'form-control',
                ],
            ])
            ->add('code', TextType::class, [
                'label' => 'Code',
                'attr' => [
                    'placeholder' => 'Ex: MATH101',
                    'class' => 'form-control',
                ],
            ])
            ->add('coefficient', NumberType::class, [
                'label' => 'Coefficient',
                'attr' => [
                    'placeholder' => 'Ex: 2',
                    'class' => 'form-control',
                    'min' => 1,
                    'max' => 10,
                    'step' => 0.5,
                ],
            ])
            ->add('volumeHoraire', IntegerType::class, [
                'label' => 'Volume Horaire (heures)',
                'attr' => [
                    'placeholder' => 'Ex: 30',
                    'class' => 'form-control',
                    'min' => 1,
                ],
            ])
            ->add('semestre', ChoiceType::class, [
                'label' => 'Semestre',
                'choices' => [
                    'Semestre 1' => 'S1',
                    'Semestre 2' => 'S2',
                    'Semestre 3' => 'S3',
                    'Semestre 4' => 'S4',
                    'Semestre 5' => 'S5',
                    'Semestre 6' => 'S6',
                ],
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
        ;
    }

    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Matiere::class,
        ]);
    }
}
