from src.Class_Tree import Tree
from src.Class_Compressor import Compressor
import graphviz
import struct


# Fontctions pour visualiser l'arbre de compression
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
	# Création d'un objet de compression avec le fichier à compresser en paramètre
	compressor1 = Compressor("donnees/alice.txt")
	compressor2 = Compressor("donnees/extraitalice.txt")
	compressor3 = Compressor("donnees/textesimple.txt")

	# Compression du fichier en utilisant l'algorithme de Huffman
	# compressor1.codage_huffman()
	compressor2.codage_huffman()
	# compressor3.codage_huffman()
