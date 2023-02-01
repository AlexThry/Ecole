from src.Class_Step import *

class Task:
	def __init__(self, name, duration, connection):
		"""Une tâche avec un nom, une durée et des connections

		Args:
			name (str): nom de la tache
			duration (int): durée de la tache
			connection (list): liste contenant l'étape de départ et l'étape d'arrivée
		"""
		self.name = name
		self.duration = duration
		# une liste contenant des tuples de la forme (etape_precedante, etape_suivante)
		self.connection = connection

	def __str__(self):
		return self.name

	def get_name(self) -> str:
		"""renvoie le nom de la tâche

		Returns:
			toStr: nom de la tâche
		"""
		return self.name

	def get_duration(self) -> int:
		"""renvoie la durée de la tâche

		Returns:
			int: durée de la tâche
		"""
		return self.duration

	def get_connection(self, toStr=False) -> tuple:
		"""permet de récupérer les étapes à laquelle une tâche est connectée

		Args:
			toStr (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

		Returns:
			tuple: les étapes connectées par la tâche
		"""
		if toStr:
			if self.connection:
				connection = (self.connection[0].get_number(
				), self.connection[1].get_number())
		else:
			if self.connection:
				connection = (self.connection[0], self.connection[1])
		return connection

	def get_begin_step(self, toStr=False):
		"""permet de récupérer l'étape dont la tâche sort

		Args:
			toStr (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

		Returns:
			l'étape précédente 
		"""
		previous_steps = []
		if toStr:
			if self.connection[0]:
				next_steps = [self.connection[0].get_number()]
		else:
			if self.connection[0]:
				next_steps = [self.connection[0]]
		return next_steps

	def get_end_step(self, toStr=False) -> list:
		"""permet de récupérer l'étape suivant la tâche

		Args:
			toStr (bool, optional): choisis si l'on renvoit le nom des étapes. Defaults to False.

		Returns:
			l'étape suivante
		"""
		next_steps = []
		if toStr:
			if self.connection[1]:
				next_steps += [self.connection[1].get_number()]
		else:
			if self.connection[1]:
				next_steps += [self.connection[1]]
		return next_steps
