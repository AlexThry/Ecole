from src.Class_Step import Step
from src.Class_Task import Task
from src.Class_PERT import PERT
import os
import matplotlib.pyplot as plt
import matplotlib.image as img

if __name__ == "__main__":

    ##_______ Création des étapes _______##

    step0 = Step(0, 0, 0)
    step1 = Step(1, 30, 30)
    step2 = Step(2, 120, 120)
    step3 = Step(3, 150, 210)
    step4 = Step(4, 40, 200)
    step5 = Step(5, 50, 210)
    step6 = Step(6, 150, 150)
    step7 = Step(7, 210, 210)
    step8 = Step(8, 220, 220)

    steps = [step0, step1, step2, step3, step4, step5, step6, step7, step8]

    ##_______ Création des tâches _______##

    taskA = Task("A", 30, (step0, step1))
    taskB = Task("B", 90, (step1, step2))
    taskC = Task("C", 30, (step2, step3))
    taskD = Task("D", 10, (step1, step4))
    taskE = Task("E", 10, (step4, step5))
    taskF = Task("F", 30, (step2, step6))
    taskG = Task("G", 60, (step6, step7))
    taskH = Task("H", 10, (step7, step8))
    taskt37 = Task("t", 0, (step3, step7))
    taskt57 = Task("t", 0, (step5, step7))

    tasks = [taskA, taskB, taskC, taskD, taskE,
             taskF, taskG, taskH, taskt37, taskt57]

    ##_______ Ajout des tâches aux étapes _______##

    step0.set_tasks([], [taskA])
    step1.set_tasks([taskA], [taskB, taskD])
    step2.set_tasks([taskB], [taskF, taskC])
    step3.set_tasks([taskC], [taskt37])
    step4.set_tasks([taskD], [taskE])
    step5.set_tasks([taskE], [taskt57])
    step6.set_tasks([taskF], [taskG])
    step7.set_tasks([taskt37, taskG, taskt57], [taskH])
    step8.set_tasks([taskH], [])

    print(f'Etape de début de la tâche B : {taskB.get_begin_step(True)}')
    print(f'Etape de début de la tâche A : {taskA.get_begin_step(True)}')
    print(f'Etape de fin de la tâche A : {taskA.get_end_step(True)}')
    print(f'Etape de fin de la tâche H : {taskH.get_end_step(True)}')

    print(f"Etapes après l'etape1 : {step1.get_next_steps(True)}")
    print(f"Etapes avant l'étape 7 : {step7.get_previous_steps(True)}")

    print(f"Tâches après l'étape 1 : {step1.get_next_tasks(True)}")
    print(f"Tâches avant l'étape 7 : {step7.get_previous_tasks(True)}")

    ##_______ Création du diagramme PERT _______##

    pert = PERT(step0)

    ##_______ Méthode critique _______##

    print(f'méthode critique sur le diagramme PERT : {pert.critique(True)}')

    ##_______ Création d'un nouvel arbre PERT sans dates au plus tôt _______##

    step0b = Step(0, None, None)
    step1b = Step(1, None, None)
    step2b = Step(2, None, None)
    step3b = Step(3, None, None)
    step4b = Step(4, None, None)

    taskAb = Task("A", 20, [step0b, step1b])
    taskBb = Task("B", 20, [step0b, step3b])
    taskCb = Task("C", 30, [step1b, step2b])
    taskDb = Task("D", 0, [step3b, step4b])
    taskEb = Task("E", 20, [step2b, step4b])

    step0b.set_tasks([], [taskAb, taskBb])
    step1b.set_tasks([taskAb], [taskCb])
    step2b.set_tasks([taskCb], [taskEb])
    step3b.set_tasks([taskBb], [taskDb])
    step4b.set_tasks([taskEb, taskDb], [])

    pert2 = PERT(step0b)

    pert2.compute_au_plus_tot()

    print(f"au plus tot etape 0 : {step0b.get_au_plus_tot()}")
    print(f"au plus tot etape 1 : {step1b.get_au_plus_tot()}")
    print(f"au plus tot etape 2 : {step2b.get_au_plus_tot()}")
    print(f"au plus tot etape 3 : {step3b.get_au_plus_tot()}")
    print(f"au plus tot etape 4 : {step4b.get_au_plus_tot()}")

    pert2.compute_au_plus_tard()

    print(f"au plus tard etape 0 : {step0b.get_au_plus_tard()}")
    print(f"au plus tard etape 1 : {step1b.get_au_plus_tard()}")
    print(f"au plus tard etape 2 : {step2b.get_au_plus_tard()}")
    print(f"au plus tard etape 3 : {step3b.get_au_plus_tard()}")
    print(f"au plus tard etape 4 : {step4b.get_au_plus_tard()}")

    path = os.getcwd()
    path2 = os.path.join(path, "assets", "Pert2.jpg")
    path3 = os.path.join(path, "assets", "Pert2-2.jpg")
    try:
        plt.figure()
        plt.subplot(1, 2, 1)
        plt.title("Diagramme Pert pour la question 4.1")
        image = img.imread(path2)
        plt.imshow(image)
        plt.subplot(1, 2, 2)
        plt.title("Diagramme rempli")
        image2 = img.imread(path3)
        plt.imshow(image2)
        plt.show()
    except FileNotFoundError:
        print("ouvrir le fichier manuellement pour voir le graph Pert2")
        print("Voir assets/Pert2.jpg pour voir le 2eme graph")
