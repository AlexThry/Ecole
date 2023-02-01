class Node:
    def __init__(self, label=None, children=[None, None], values=[]) -> None:
        """Un noeud

        Args:
            label (int, optional): label du noeud. Defaults to None.
            children (list, optional): liste des enfents du noeud. Defaults to [None, None].
            values (list, optional): Une liste de valeur pour créer un noeud racine et tous ses décendants dans un arbre binaire de recherche équilibré. Defaults to [].
        """
        if not values and label:
            self.label = label
            self.children = children
        elif len(values) == 1:
            self.label = values[0]
            self.children = children
        elif len(values) == 2:
            self.label = values[0]
            if values[1] > self.label:
                self.children = [None, Node(values[1])]
            else:
                self.children = [Node(values[1]), None]
        elif len(values) > 2:
            self.label = median(values)[0]
            leftChild = Node(values=median(values)[1])
            rightChild = Node(values=median(values)[2])
            self.set_children([leftChild, rightChild])

    def content(self) -> any:
        """renvoie le(s) label(s) du noeud

        Returns:
            str: labal(s) du noeud
        """
        return self.label

    def children(self) -> list:
        """renvoie la liste des noeuds enfants

        Returns:
            list: la liste des enfants du noeud
        """
        return self.children

    def set_children(self, children=[None, None]) -> None:
        """permet de changer les enfants d'uun noeud

        Args:
            children (list, optional): liste contenant les deux enfants du noeud. Defaults to [None, None].
        """
        self.children = children
        
    def set_left_children(self, left_children):
        self.children[0] = left_children
        
    def set_right_children(self, right_children):
        self.children[1] = right_children
       
    def add_value(self, value):
        # si la valeur à ajouter est inférieure à la valeur du noeud actuel, on traite le fils de gauche
        if value.label < self.label:
            #si il y a un fils gauche, on lui applique la méthode
            if self.children[0]: 
                self.children[0].add_node(Node(value))
            #sinon, on crée ce fils de gauche avec la valeur
            else: 
                value.children = [None, None]
                self.children[0] = value
        # si la valeur à ajouter est supérieur à la valeur du noeud actuel, on traite le fils de droite
        elif value.label > self.label:
            if self.children[1]: 
                self.children[1].add_node(Node(value))
            else: 
                value.children = [None, None]
                self.children[1] = value
        else:
            return "cette valeur appartient dejà à l'arbre"
            
        # def add_value(self, value):
        #     self.add_node(Node(value))
        # print("coucou")
        # if value == self.label:
        #     return "cette valeur appartient dejà à l'arbre"
            
        # elif value < self.label:
        #     if not self.children[0]:
        #         self.children[0] = Node(values=[value])
        #     else:
        #         self.children[0].add_value(value)
            
        # else:
        #     if not self.children[1]:
        #         self.children[1] = Node(values=[value])
        #         print(self.children)
        #         print(self.children[1].children)
        #     else:
        #         self.children[1].add_value(value)
            
      
       
        
class ABR:
    def __init__(self, root=None, values=[]) -> None:
        """un arbre binaire de recherche équilibré

        Args:
            root (Node, optional): Noeud racine qui définit m'arborescence. Defaults to None.
            values (list, optional): liste de valeurs afin de créer un arbre bianire de recherche équilibré. Defaults to [].
        """
        if root:
            self.root = root
        elif values:
            self.root = Node(values=values)

    def get_root(self) -> Node:
        """renvoie la raçine d'un noeud

        Returns:
            Node: Noeud racine de l'ABR
        """
        return self.root

    def existe(self, value, compteur=1):
        """Renvoie si une valeur existe dans l'arbre ainsi que le nombre d'itérations nécéssaire pour la trouver.

        Args:
            value (str): valeur recherchée

        Returns:
            tuple: renvoie si la valleur recherchée existe et le nombre d'itérations nécéssaires pour la trouver.
        """
        if value == self.root.content():
            return (True, compteur)
        elif value < self.root.content() and self.root.children and self.root.children[0] != None:
            return ABR(self.root.children[0]).existe(value, compteur+1)
        elif value > self.root.content() and self.root.children and self.root.children[1] != None:
            return ABR(self.root.children[1]).existe(value, compteur+1)

        return False
    
    def get_values(self):
        label = [self.root.content()]
        left_child = self.root.children[0]
        right_child = self.root.children[1]
        if left_child:
                if left_child.children:
                    label += ABR(left_child).get_values()
                else:
                    label.append(left_child.content())
        if right_child:
                if right_child.children:
                    label += ABR(right_child).get_values()
                else:
                    label.append(right_child.content())
        return label
        
    
    def add_value(self, value) -> None:
        self.root.add_value(value)
        
    def balance(self):
        return ABR(values=self.get_values())
            
            
            

def existe(liste, valeur):
    """cherche si une valeur existe dans une liste

    Args:
        liste (list): liste de valeurs dans laquelle on fait une recherche
        valeur (any): valeur recherchée dans la liste

    Returns:
        (bool, int): résultat de la recherche et nombre d'itérations pour la terminer (=-1 si pas trouvée)
    """
    found = False
    i = 0
    while i < len(liste) and not found:
        if liste[i] == valeur:
            found = True
        i += 1
    if not found:
        i = -1
    return (found, i)


def median(values):
    """retourne dans un tuple la valeur mediane d'une liste, la liste des valeurs avant la médiane et la liste des valeurs après la médiane

    Args:
        values (liste): liste de valeurs non triées

    Returns:
        tuple: (median,valeurs avant la mediane, valeurs apres la mediane)
    """
    values.sort()
    if len(values) % 2 != 0:
        return (values[len(values)//2], values[:len(values)//2], values[len(values)//2 + 1:])
    else:
        return (values[len(values)//2 - 1], values[:len(values)//2 - 1], values[len(values)//2:])


if __name__ == "__main__":
    node1 = Node(1)
    node4 = Node(4)
    node7 = Node(7)
    node10 = Node(10)
    node3 = Node(3, [None, node4])
    node9 = Node(9, [None, node10])
    node6 = Node(6, [None, node7])
    node2 = Node(2, [node1, node3])
    node8 = Node(8, [node6, node9])
    node5 = Node(5, [node2, node8])
    Abr = ABR(node5)

    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # print("liste")
    # print("valeur = 1")
    # print(existe(liste, 1))
    # print("valeur = 2")
    # print(existe(liste, 2))
    # print("valeur = 3")
    # print(existe(liste, 3))
    # print("valeur = 4")
    # print(existe(liste, 4))
    # print("valeur = 5")
    # print(existe(liste, 5))
    # print("valeur = 6")
    # print(existe(liste, 6))
    # print("valeur = 7")
    # print(existe(liste, 7))
    # print("valeur = 8")
    # print(existe(liste, 8))
    # print("valeur = 9")
    # print(existe(liste, 9))
    # print("valeur = 10")
    # print(existe(liste, 10))
    # print("ABR")
    # print("valeur = 1")
    # print(Abr.existe(1))
    # print("valeur = 2")
    # print(Abr.existe(2))
    # print("valeur = 3")
    # print(Abr.existe(3))
    # print("valeur = 4")
    # print(Abr.existe(4))
    # print("valeur = 5")
    # print(Abr.existe(5))
    # print("valeur = 6")
    # print(Abr.existe(6))
    # print("valeur = 7")
    # print(Abr.existe(7))
    # print("valeur = 8")
    # print(Abr.existe(8))
    # print("valeur = 9")
    # print(Abr.existe(9))
    # print("valeur = 10")
    # print(Abr.existe(10))
    # print("valeur = 11")
    # print(Abr.existe(11))

    # print(median([1, 2, 3, 4, 5, 6, 7]))
    # print(median([1, 2, 3, 4, 5, 6, 7, 8]))

    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[0].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[1].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[0].children[0].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[0].children[1].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[1].children[0].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[1].children[1].content())
    # print(Node(values=[1, 2, 3, 4, 5, 6, 7, 8]).children[1].children[1].children[1].content())

    abr = ABR(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11])
    
    # print(abr.root.content())
    # print(abr.root.children[0].content())
    # print(abr.root.children[1].content())
    # print(abr.root.children[0].children[0].content())
    # print(abr.root.children[0].children[1].content())
    # print(abr.root.children[1].children[0].content())
    # print(abr.root.children[1].children[1].content())
    # print(abr.root.children[0].children[1].children[1].content())
    # print(abr.root.children[1].children[0].children[1].content())
    # print(abr.root.children[1].children[1].children[1].content())


    
    # print(abr.existe(1))

    print(Abr.get_values())
    # print(abr.get_values())
    
    arbre1 = ABR(values=[1,2,3,5,6])
    print(arbre1.get_values())
    
    # Abr.add_value(20)
    # print(Abr.get_values())
    
    
    arbre1.add_value(4)
    print(arbre1.get_values())
    arbre1.add_value(8)
    print(arbre1.get_values())

    
    # print(arbre1.get_values())

    
    # print(arbre1.root.content())
    # print(arbre1.root.children[0].content())
    # print(arbre1.root.children[1].content())
    # print(arbre1.root.children[1].children[1].content())
    # print(arbre1.root.children[0].children[1].content())

    
    