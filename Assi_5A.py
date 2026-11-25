class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def inorder(self):
        stack = []
        temp = self.root

        while temp is not None or len(stack) > 0:

            while temp is not None:
                stack = stack + [temp]
                temp = temp.left

            temp = stack[-1]
            stack = stack[:-1]

            print(temp.data, end=" ")

            temp = temp.right

    def preorder(self):
        if self.root is None:
            print("Tree is empty")
            return

        stack = [self.root]

        while len(stack) > 0:
            temp = stack[-1]
            stack = stack[:-1]

            print(temp.data, end=" ")

            if temp.right is not None:
                stack = stack + [temp.right]

            if temp.left is not None:
                stack = stack + [temp.left]


bst = BST()

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    bst.insert(data)

print("\nInorder Traversal:")
bst.inorder()

print("\nPreorder Traversal:")
bst.preorder()