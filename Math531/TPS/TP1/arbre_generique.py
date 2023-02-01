class Node:
  def __init__(self, labels, children=[]) -> None:
    """Crée un noeud

    Args:
        labels (str): labels du noeud
        children (list, optional): _description_. Defaults to [].
    """
    self.labels = labels
    self.children = children
  
  
  def content(self) -> str:
    """Retourne le label du noeud

    Returns:
        str: lablel du noeud
    """
    return self.labels
  
  def children(self) -> list:
    return self.children

class RTree:
  def __init__(self, root) -> None:
    """Crée une arborescence

    Args:
        root (Node): la racine de l'arborescence
    """
    self.root = root
        
  def root(self) -> Node:
    """retourne la racine de l'arborescence

    Returns:
        Node: racine de l'arborescence
    """
    return self.root
  
  def sub_tree(self) -> list:
    """_summary_

    Returns:
        list: _description_
    """
    sub_trees = []
    for i in self.root.children:
      sub_trees.append(RTree(i))
    return sub_trees
  
  def is_empty(self) -> bool:
    return not bool(self.sub_tree())
    
  def display_depth(self):
    label = [self.root.content()]
    for node in self.root.children:
      if bool(node.children):
        label += RTree(node).display_depth()
      else:
        label.append(node.content())
    return label
  
  def display_width(self):
    label = []
    if self.is_empty():
      label.append(self.root.content())
    else:
      forest = Forest([self])
      return forest.width_browse()
      
    
class Forest:
  def __init__(self, trees):
    self.trees = trees
    
  def is_empty(self):
    return not bool(self.trees)
  
  def first_tree(self):
    return self.trees[0]
    
  def width_browse(self):
    label = []
    if self.is_empty():
      return None
    else:
      node = self.first_tree().root()
      
  
    
if __name__ == "__main__":
  node6 = Node("9")
  node5 = Node("3")
  node4 = Node("3")
  node3 = Node("m")
  node2 = Node("a")
  node1 = Node("2", [node4, node5, node6])
  node0 = Node("z", [node1, node2, node3])
  tree = RTree(node0)
  tree2 = RTree(node6)
  forest = [tree, tree2]
  
  print(tree.display_depth())
  