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


def preorder_nonrecursive(root):
    if root is None:
        print("Tree is empty")
        return

    stack = [None] * 100
    top = -1

    top = top + 1
    stack[top] = root

    print("Preorder Traversal:")

    while top != -1:
        temp = stack[top]
        top = top - 1

        print(temp.data)

        if temp.right is not None:
            top = top + 1
            stack[top] = temp.right

        if temp.left is not None:
            top = top + 1
            stack[top] = temp.left


root = None

n = int(input("Enter number of students: "))

for i in range(n):
    data = int(input("Enter admission number: "))
    root = insert(root, data)

preorder_nonrecursive(root)

print("-------------------------------------")