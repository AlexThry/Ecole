from src.Class_Tree import Tree
from src.Class_Compressor import Compressor
import graphviz

def visualize_tree(tree):
	graph = graphviz.Graph(format="png")
	add_nodes(tree.root, graph)
	return graph

def add_nodes(node, graph):
	if node is None:
		return
	graph.node(str(id(node)), label=node.label)
	if node.left_child is not None:
		graph.edge(str(id(node)), str(id(node.left_child)), "0")
		add_nodes(node.left_child, graph)
	if node.right_child is not None:
		graph.edge(str(id(node)), str(id(node.right_child)), "1")
		add_nodes(node.right_child, graph)

if __name__ == "__main__":
	tree = Tree("donnees/textesimple.txt")
	visualize_tree(tree).render()
	compresor = Compressor("donnees/textesimple.txt")

