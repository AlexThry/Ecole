class Node:
	def __init__(self, label, frequence, left_child=None, right_child=None):
		self.label = label
		self.frequence = frequence
		self.left_child = left_child
		self.right_child = right_child

	def parcours_profondeur(self, code=""):
		if self.left_child:
			code += '0'
			self.left_child.parcours_profondeur(code)
		if self.right_child:
			code += '1'
			self.right_child.parcours_profondeur(code)
		if not self.left_child and not self.right_child:
			return code

	def __lt__(self, node):
		return self.frequence < node.frequence

	def __gt__(self, node):
		return self.frequence > node.frequence
		
		