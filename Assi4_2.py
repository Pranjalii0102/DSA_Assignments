class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = input("Enter department (0 to stop): ")

    if x == "0":
        return None

    root = Node(x)

    print("Enter left of", x)
    root.left = create()

    print("Enter right of", x)
    root.right = create()

    return root


def postorder_nonrecursive(root):
    if root is None:
        print("Tree is empty")
        return

    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) != 0:
        temp = stack1.pop()
        stack2.append(temp)

        if temp.left is not None:
            stack1.append(temp.left)

        if temp.right is not None:
            stack1.append(temp.right)

    print("Non-Recursive Postorder:")

    while len(stack2) != 0:
        temp = stack2.pop()
        print(temp.data)


root = create()

postorder_nonrecursive(root)

print("-------------------------------------")