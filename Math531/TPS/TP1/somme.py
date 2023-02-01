def factorielle(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorielle(n-1)
  
def somme(n):
  if n == 0:
    return 0
  else:
    return n + somme(n-1)
  
def reverse(a):
  if len(a) == 1:
    return a
  else:
    return a[len(a)-1] + reverse(a[:len(a)-1])
  
def puissance(n, p):
  if p == 0:
    return 1
  elif p == 1:
    return n
  else:
    return n * puissance(n, p-1)
  
def longueur(char):
  if not bool(char):
    return 0
  else:
    return 1 + longueur(char[1:])
  
def somme2(n):
  if n == 0:
    return 0
  else:
    return n + somme2(n-1)
  
def binaire(n):
  if n == 0:
    return []
  else:
    return binaire(n//2) + [n%2]
  
def suite(n):
  if n < 2:
    return 1
  else:
    return 3*suite(n-1)+suite(n-2)
  
class Node:
  def __init__(self, label, children=[]):
    self.label = label
    self.children = children
  
  def descendre(self):
    current_node = self
    if bool(current_node.children):
      current_node = current_node.children[0]
      return current_node.descendre()
    else:
      return current_node.label      
      
    
def pair(n):
  if n == 1:
    return False
  else:
    return impair(n-1)
  
def impair(n):
  if n == 1:
    return True
  else:
    return pair(n-1)
  
def maximum(tab):
  if len(tab) == 1:
    return tab[0]
  elif not bool(tab):
    return None
  else:
    m = len(tab)//2
    max1 = maximum(tab[:m])
    max2 = maximum(tab[m:])
    if max1 > max2:
      return max1
    return max2
    
  
  
  
if __name__ == "__main__":
  print(factorielle(10))
  print(factorielle(0))
  
  print(somme(5))
  print(somme(10))
  
  print(reverse("abcde"))
  print(reverse("alexis"))
  
  
  node6 = Node(6)
  node5 = Node(5, [node6])
  node4 = Node(4, [node5])
  node3 = Node(3, [node4])
  node2 = Node(2, [node3])
  node1 = Node(1, [node2])
  
  print(node1.descendre())
  
  print(puissance(10, 1))
  
  print(longueur("abcdef"))
  
  print(somme2(6))
  
  print(binaire(4))
  
  print(suite(2))
  
  print(pair(5))
  print(pair(4))

  print(impair(5))
  print(impair(4))
  
  print(maximum([1,5,3,6,2]))

