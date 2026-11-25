class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        q = [self.root]

        while len(q) > 0:
            temp = q[0]
            q = q[1:]

            if temp.left is None:
                temp.left = new_node
                return
            else:
                q = q + [temp.left]

            if temp.right is None:
                temp.right = new_node
                return
            else:
                q = q + [temp.right]

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

while True:
    print("\n1. Insert Book")
    print("2. Inorder Navigation")
    print("3. Preorder Navigation")
    print("4. Postorder Navigation")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = input("Enter book name: ")
        bt.insert(data)

    elif choice == 2:
        print("Inorder:")
        bt.inorder(bt.root)
        print()

    elif choice == 3:
        print("Preorder:")
        bt.preorder(bt.root)
        print()

    elif choice == 4:
        print("Postorder:")
        bt.postorder(bt.root)
        print()

    elif choice == 5:
        break

    else:
        print("Invalid choice")