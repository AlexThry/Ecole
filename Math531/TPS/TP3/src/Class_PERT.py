class PERT:
    def __init__(self, root):
        self.root = root

    def critique(self, toStr=False, critique=[]):
        """renvoie le chemin critique d'un diagramme PERT

        Args:
                        toStr (bool, optional): permet de renvoyer les noms des objets au lieu des objets eux même. Defaults to False.
                        critique (list, optional): liste mise a jour. Defaults to [].

        Returns:
                        list: liste contenant les étapes du chemin critique
        """
        if not critique:
            if toStr:
                critique.append(self.root.get_number())
            else:
                critique.append(self.root)
        if not self.root.get_next_steps():
            return critique
        else:
            for step in self.root.get_next_steps():
                if step.get_au_plus_tard() == step.get_au_plus_tot():
                    new_step = step
            if toStr:
                critique.append(new_step.get_number())
            else:
                critique.append(new_step)
            return PERT(new_step).critique(toStr, critique)

    def compute_au_plus_tot(self):
        """calcule les dates au plus tot de chaque étape pour une diagramme PERT sans dates
        """
        if not self.root.get_previous_steps():
            self.root.set_au_plus_tot(0)
        for task in self.root.get_next_tasks():
            if self.root.get_next_tasks() and (not(task.get_end_step()[0].get_au_plus_tot()) or task.get_end_step()[0].get_au_plus_tot() < task.get_begin_step()[0].get_au_plus_tot() + task.get_duration()):
                task.get_end_step()[0].set_au_plus_tot(task.get_begin_step()[
                    0].get_au_plus_tot() + task.get_duration())
            PERT(task.get_end_step()[0]).compute_au_plus_tot()

    def compute_au_plus_tard(self):
        """calcule les dates au plus tard
        """
        self.compute_au_plus_tot()
        if not self.root.get_next_steps():
            self.root.set_au_plus_tard(self.root.get_au_plus_tot())
        for task in self.root.get_next_tasks():
            duration = task.get_duration()
            next_step = task.get_end_step()[0]
            self.root.set_au_plus_tard(next_step.get_au_plus_tot()-duration)
            PERT(next_step).compute_au_plus_tard()
