from anytree import Node, RenderTree

raiz = Node(5)
derecha = Node(6, parent =raiz)

print(RenderTree(raiz))