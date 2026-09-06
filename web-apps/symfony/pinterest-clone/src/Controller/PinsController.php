<?php

namespace App\Controller;



use App\Entity\Pin;
use App\Form\PinType;
use App\Repository\PinRepository;
use Doctrine\ORM\EntityManagerInterface;
use PhpParser\Builder\Method;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Form\Extension\Core\Type\TextareaType;
use Symfony\Component\Form\Extension\Core\Type\TextType as TypeTextType;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class PinsController extends AbstractController
{
    /**
     * @Route("/", name="app_home",methods="GET")
     */
    public function index(PinRepository $pinRepository): Response
    {
        $pins = $pinRepository->findBy([], ['createdAt' => 'DESC']);
        return $this->render('pins/index.html.twig', compact('pins'));
    }
    /**
     *  @Route("/pins/{id<[0-9]+>} ", name="app_pins_show",methods="GET")
     */
    public function show(Pin $pin): Response
    {
        return $this->render('pins/show.html.twig', compact('pin'));
    }
    /**
     *  @Route("/pins/create", name="app_pins_create",methods="GET|POST")
     */
    public function create(Request $request, EntityManagerInterface $em): Response
    {
        $data = new Pin;
        $form = $this->createForm(PinType::class, $data);

        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $data->setUser($this->getUser());
            $em->persist($data);
            $em->flush();

            $this->addFlash('Success', 'Pin crée avec succes');
            return $this->redirectToRoute('app_home');
        }
        return $this->render('pins/create.html.twig', ['form' => $form->createView()]);
    }
    /**
     *  @Route("/pins/{id<[0-9]+>}/edit ", name="app_pins_edit",methods="GET|PUT")
     */
    public function edit(Request $request,   Pin $pin, EntityManagerInterface $em): Response
    {
        $form = $this->createForm(PinType::class, $pin, ['method' => 'PUT']);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {

            $em->flush();
            $this->addFlash('Success', 'Pin modifié avec succes');

            return $this->redirectToRoute('app_home');
        }

        return $this->render('pins/edit.html.twig', ['deform' => $form->createView(), 'op' => $pin]);
    }
    /**
     *  @Route("/pins/{id<[0-9]+>}/delete", name="app_pins_delete",methods="DELETE")
     */
    public function delete(Request $request,   Pin $pin, EntityManagerInterface $em): Response
    {
        if ($this->isCsrfTokenValid('pin_deletion_' . $pin->getId(), $request->request->get('csrf_token'))) {
            $em->remove($pin);
            $em->flush();

            $this->addFlash('Info', 'Pin supprimé');
        }
        return $this->redirectToRoute('app_home');
    }
}
