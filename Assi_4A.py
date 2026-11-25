class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self):
        data = int(input("Enter data (-1 for no node): "))

        if data == -1:
            return None

        new_node = Node(data)

        print("Enter left child of", data)
        new_node.left = self.create()

        print("Enter right child of", data)
        new_node.right = self.create()

        return new_node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


bt = BinaryTree()

bt.root = bt.create()

print("\nInorder:")
bt.inorder(bt.root)

print("\nPreorder:")
bt.preorder(bt.root)

print("\nPostorder:")
bt.postorder(bt.root)