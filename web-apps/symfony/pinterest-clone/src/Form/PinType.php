<?php

namespace App\Form;

use App\Entity\Pin;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;
use Vich\UploaderBundle\Form\Type\VichImageType;




use Liip\ImagineBundle\DependencyInjection\LiipImagineExtension;
use Liip\ImagineBundle\LiipImagineBundle;
use Symfony\Component\Form\Extension\Core\Type\TextareaType;

use Symfony\Config\LiipImagineConfig;


class PinType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options): void
    {
        $builder
            ->add('title')
            ->add('description')
            ->add('imageFile', VichImageType::class, [
                'label' => 'Image(Png etg Jpg files)',
                'required' => false,
                'allow_delete' => true,
                'delete_label' => 'Delete',
                'download_label' => 'Telecharger',
                'download_uri' => false,
                'image_uri' => true,
                'imagine_pattern' => 'squared_thumbnail_medium',
                'asset_helper' => true,
            ]);
    }
    public function configureOptions(OptionsResolver $resolver): void
    {
        $resolver->setDefaults([
            'data_class' => Pin::class,
        ]);
    }
}
