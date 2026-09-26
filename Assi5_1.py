class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


root = None

n = int(input("Enter number of books: "))

for i in range(n):
    data = int(input("Enter book ID: "))
    root = insert(root, data)

print("\nPreorder Traversal:")
preorder(root)

print("-------------------------------------")