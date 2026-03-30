<?php

namespace App\Form;

use App\Entity\Etudiant;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\EmailType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class EtudiantType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('nom', TextType::class, [
                'label' => 'Nom',
                'attr' => [
                    'placeholder' => 'Entrez le nom',
                    'class' => 'form-control',
                ],
            ])
            ->add('prenom', TextType::class, [
                'label' => 'Prénom',
                'attr' => [
                    'placeholder' => 'Entrez le prénom',
                    'class' => 'form-control',
                ],
            ])
            ->add('numeroEtudiant', TextType::class, [
                'label' => 'Numéro Étudiant',
                'attr' => [
                    'placeholder' => 'Ex: ET2024001',
                    'class' => 'form-control',
                ],
            ])
            ->add('email', EmailType::class, [
                'label' => 'Email',
                'attr' => [
                    'placeholder' => 'etudiant@exemple.com',
                    'class' => 'form-control',
                ],
            ])
            ->add('dateNaissance', DateType::class, [
                'label' => 'Date de Naissance',
                'widget' => 'single_text',
                'attr' => [
                    'class' => 'form-control',
                ],
            ])
            ->add('niveau', ChoiceType::class, [
                'label' => 'Niveau',
                'choices' => [
                    'Licence 1' => 'L1',
                    'Licence 2' => 'L2',
                    'Licence 3' => 'L3',
                    'Master 1' => 'M1',
                    'Master 2' => 'M2',
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
            'data_class' => Etudiant::class,
        ]);
    }
}
