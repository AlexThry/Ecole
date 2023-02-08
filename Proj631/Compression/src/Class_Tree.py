from src.Class_File import File
from src.Class_Node import Node

class Tree:
	def __init__(self, file):
		self.create_leaves(file)
		self.root = self.create_root(self.leaves)

	def create_leaves(self, file):
		file = File(file)
		dico = dict(file.frequence)
		alphabet_nodes = []
		characters = dico.keys()
		frequences = dico.values()
		for char, freq in zip(characters, frequences):
			alphabet_nodes.append(Node(char, freq, None, None))
		self.leaves = alphabet_nodes

	def get_two_smallest(self, nodes):
		t1 = nodes[0]
		t2 = nodes[1]
		if t1 > t2:
			t1, t2 = t2, t1
		for node in nodes[2:]:
			if node < t1:
				t2 = t1
				t1 = node
			elif node < t2:
				t2 = node
		return t1, t2

	def create_root(self, nodes):
		if len(nodes) == 1:
			return nodes[0]
		else:
			t1, t2 = self.get_two_smallest(nodes)
			t = Node(str(t1.frequence + t2.frequence), t1.frequence + t2.frequence, t1, t2)
			nodes.append(t)
			del nodes[nodes.index(t1)]
			del nodes[nodes.index(t2)]
			return self.create_root(nodes)
	def parcours_profondeur(self):
		self.root.parcours_profondeur()

if __name__ == "__main__":
	tree = Tree("/Users/alexisthierry/Documents/Alex/Cours/code/GitHub/Ecole/Proj631/Compression/donnees/alice.txt")
	print(tree.root.frequence)
