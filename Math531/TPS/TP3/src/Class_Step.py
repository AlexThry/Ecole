class Step:
	"""Une étape ayant un numéro, une date à laquelle elle peut être passée au plus tôt et une date à laquelle elle peut être passée au plus tard.
			Elle contient aussi la liste de ses taches entrantes et la liste de ses teches sortantes.
	"""

	def __init__(self, number, au_plus_tot=None, au_plus_tard=None, previous_tasks=None, next_tasks=None):
		self.number = number
		self.au_plus_tot = au_plus_tot
		self.au_plus_tard = au_plus_tard

	def __str__(self):
		return self.number

	def get_au_plus_tot(self) -> int:
		"""renvoie la date à laquelle l'étape peut être éxécutée au plus tôt

		Returns:
						int: date au plus tot
		"""
		return self.au_plus_tot

	def get_au_plus_tard(self) -> int:
		"""renvoie la date à laquelle l'étape peut être éxécutée au plus tôt

		Returns:
						int: date au plus tard
		"""
		return self.au_plus_tard

	def set_au_plus_tot(self, date) -> None:
		"""permet de définir la date au plus tôt

		Args:
			date (int): date au plus tôt
		"""
		self.au_plus_tot = date

	def set_au_plus_tard(self, date) -> None:
		"""permet de définir la date au plus tard

		Args:
			date (int): date au plus tard
		"""
		self.au_plus_tard = date

	def set_tasks(self, previous_tasks=[], next_tasks=[]) -> None:
		"""permet de mettre en place les taches entrantes et les taches sortantes

		Args:
						previous_tasks (list, optional): liste des taches entrantes. Defaults to [].
						next_tasks (list, optional): liste des taches sortantes. Defaults to [].
		"""
		self.previous_tasks = previous_tasks
		self.next_tasks = next_tasks

	def add_previous_task(self, task=None, tasks=[]) -> None:
		"""permet d'ajouter une ou des tâches à la liste des tâches précédentes

		Args:
						task (Task, optional): ajout d'une tache unique. Defaults to None.
						tasks (list, optional): ajout d'une liste de tache. Defaults to [].
		"""
		if task:
			self.previous_tasks.append(task)
		elif tasks:
			self.previous_tasks += tasks

	def add_next_task(self, task=None, tasks=[]) -> None:
		"""permet d'ajouter une ou des tâches à la liste des tâches suivantes

		Args:
						task (Task, optional): ajout d'une tache unique. Defaults to None.
						tasks (list, optional): ajout d'une liste de tache. Defaults to [].
		"""
		if task:
			self.next_tasks.append(task)
		elif tasks:
			self.next_tasks += tasks

	def get_number(self) -> int:
		"""permet de récupérer le numéro de l'étape

		Returns:
						int: numéro de l'étape
		"""
		return self.number

	def get_next_steps(self, toStr=False) -> list:
		"""permet de récupérer la liste de étapes suivantes

		Args:
						toStr (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

		Returns:
						list: liste des étapes suivantes
		"""
		next_steps = []
		if self.next_tasks:
			for task in self.next_tasks:
				if toStr:
					next_steps += task.get_end_step(True)
				else:
					next_steps += task.get_end_step()
		return next_steps

	def get_previous_steps(self, toStr=False) -> list:
		"""permet de récupérer la liste de étapes précédentes

		Args:
						toStr (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

		Returns:
						list: liste des étapes précédentes
		"""
		previous_steps = []
		if self.previous_tasks:
			for task in self.previous_tasks:
				if toStr:
					previous_steps += task.get_begin_step(True)
				else:
					previous_steps += task.get_begin_step()
		return previous_steps

	def get_next_tasks(self, toStr=False):
		if toStr:
			liste = []
			for task in self.next_tasks:
				liste.append(task.get_name())
		else:
			liste = self.next_tasks

		return liste

	def get_previous_tasks(self, toStr = False):
		if toStr:
			liste = []
			for task in self.previous_tasks:
				liste.append(task.get_name())
		else:
			liste = self.previous_tasks

		return liste

	
