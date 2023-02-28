class Node:
	def __init__(self, label, frequence, left_child=None, right_child=None):
		self.label = label
		self.frequence = frequence
		self.left_child = left_child
		self.right_child = right_child

	def parcours_profondeur(self, char, code=""):
		if self.label == char:
			return code
		if self.left_child:
			code_left = self.left_child.parcours_profondeur(char, code + "0")
			if code_left:
				return code_left
		if self.right_child:
			return self.right_child.parcours_profondeur(char, code + "1")
		return None



	def __lt__(self, node):
		return self.frequence < node.frequence

	def __gt__(self, node):
		return self.frequence > node.frequence
		
		