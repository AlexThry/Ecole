class Node:
  def __init__(self, label, children=[]):
    self.label = label
    self.children = children
    
  def content(self):
    return self.label
  
  def is_empty(self):
    return not bool(self.children)
  
class RTree:
  def __init__(self, root):
    self.root = root
  
  def root(self):
    return self.root
  
  def sub_tree(self):
    trees = []
    for tree in self.root.children:
      trees.append(tree)
    return trees
  
  def display_depth(self):
    labels = [self.root.content()]
    for child in self.root.children:
      if child.children:
        labels += RTree(child).display_depth()
      else:
        labels.append(child.content())
    return labels 
  

      
  
  
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
  
  liste = [1,2,3,4]
  print(liste[:1])
  print(liste[1:])
  
  # print(tree.display_depth())
  # print(tree.display_width())