class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = input("Enter patient registration number (0 to stop): ")

    if x == "0":
        return None

    root = Node(x)

    print("Enter left of", x)
    root.left = create()

    print("Enter right of", x)
    root.right = create()

    return root


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root = create()

print("\nPostorder Traversal:")
postorder(root)

print("-------------------------------------")