# Name: Ishan Nandal
# Student ID: 28278046


class Node:
    def __init__(self, string, value):
        self.string = string
        self.value = value
        self.left = None
        self.right = None
        self.path = ""


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


if __name__ == "__main__":
    node1 = Node('c', 10)
    print(node1.string, node1.value)
    tree1 = BinaryTree(node1)
    print(tree1.root.value)
