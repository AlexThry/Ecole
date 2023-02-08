from Class_File import File
from Class_Node import Node

class Tree:
	def __init__(self, file):
		self.create_leaves()

	def create_leaves(self, file):
		file = File(file)
		alphabet_nodes = []
		characters = file.frequence.keys()
		frequences = file.frequence.values()
		for char, freq in zip(characters, frequences):
			alphabet_nodes.append(Node(char, freq, None, None))
		self.leaves = alphabet_nodes
	def get_root(self):
		return self.root

	def parcours_profondeur(self):
		self.root.parcours_profondeur()
