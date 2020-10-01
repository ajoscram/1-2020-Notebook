class Node:
    def __init__(self, num = None):
        self.izq = None
        self.der = None
        self.num = num

root = Node(10)
root.izq = Node(4)
root.izq.izq = Node(2)
root.izq.izq.izq = Node(1)
root.izq.der = Node(8)
root.izq.der.izq = Node(6)
root.izq.der.der = Node(9)
root.der = Node(20)
root.der.izq = Node(14)
root.der.der = Node(25)
root.der.der.izq = Node(23)
root.der.der.izq = Node(28)

def DepthSearch(node, num, visited=[]):
    visited.append(node.num)
    if(node.num == num):
        return visited
    else:
        if(node.izq):
            DepthSearch(node.izq, num, visited)
        if(node.der):
            DepthSearch(node.der, num, visited)

def BreadthSearch(node, numero, visitados=[]):
  print(node.num)
  if(node.num == numero):
    print(True)
    return True
  else:
    if(node.izq):
      DepthSearch(node.izq, numero)
    if(node.der):
      DepthSearch(node.der, numero)

print(DepthSearch(root, 28))