from Classes.Class_Tree import Tree
from Classes.Class_Node import Node


def read_file(file):
	with open(file, "r") as f:
		lignes = f.read()
	return lignes


def frequence_apparition(str):
	frequence = {}
	for i in str:
		if i not in frequence.keys():
			frequence[i] = 1
		else:
			frequence[i] += 1
	return frequence


def frequence_apparitionic(frequence):
	frequence = dict(sorted(frequence.items(), key=lambda t: t[0]))
	return sorted(frequence.items(), key=lambda t: t[1])


def write_frequence(file):
	list_freq = frequence_apparitionic(frequence_apparition(read_file(file)))
	with open(file[:-4]+"_freq.txt", "w") as f:
		f.write(str(len(frequence)) + "\n")
		for item in list_freq:
			char = item[0]
			freq = str(item[1])
			f.write(f"{char} {freq} \n")


def create_leafs(file):
	alphabet_nodes = []
	frequence = dict(frequence_apparitionic(
		frequence_apparition(read_file(file))))
	characters = frequence.keys()
	frequences = frequence.values()
	for char, freq in zip(characters, frequences):
		alphabet_nodes.append(Node(char, freq, None, None))
	return alphabet_nodes


def is_power_2(n):
	res = n
	while res > 1:
		res = res/2
	if res == 1:
		return True
	else:
		return False


def create_root(nodes):
	if len(nodes) == 1:
		return nodes[0]
	else:
		t1 = nodes[0]
		t2 = nodes[1]
	for node in nodes:
		if node.frequence < t2.frequence:
			t2 = node
			if node.frequence < t1.frequence:
				t1 = node
	t = Node('', t1.frequence+t2.frequence, t1, t2)
	new_nodes = [t]
	for node in nodes:
		if node != t1 and node != t2:
			new_nodes.append(node)
	return create_root(new_nodes)


	


if __name__ == "__main__":
	alice = read_file("donnees/alice.txt")
	frequence = frequence_apparition(alice)
	write_frequence("donnees/alice.txt")
	alphabet_nodes = create_leafs('donnees/alice.txt')
	root = create_root(alphabet_nodes)
	print(root.frequence)
	tree = Tree(root)

