class Tree:
	def __init__(self, root):
		self.root = root

	def get_root(self):
		return self.root

	def parcours_profondeur(self):
		self.root.parcours_profondeur()
