class Node:
    def __init__(self, adm_no, name):
        self.adm_no = adm_no
        self.name = name
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, adm_no, name):
        new_node = Node(adm_no, name)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if adm_no < temp.adm_no:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left

            elif adm_no > temp.adm_no:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

            else:
                print("Admission number already exists")
                return

    def search(self, adm_no):
        temp = self.root

        while temp is not None:
            if adm_no == temp.adm_no:
                print("Student Found")
                print("Admission Number:", temp.adm_no)
                print("Name:", temp.name)
                return

            elif adm_no < temp.adm_no:
                temp = temp.left

            else:
                temp = temp.right

        print("Student not found")

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.adm_no, "-", node.name)
            self.inorder(node.right)


bst = BST()

while True:
    print("\n1. Insert Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        adm_no = int(input("Enter admission number: "))
        name = input("Enter student name: ")
        bst.insert(adm_no, name)

    elif choice == 2:
        adm_no = int(input("Enter admission number to search: "))
        bst.search(adm_no)

    elif choice == 3:
        print("\nStudents in Admission Number Order:")
        bst.inorder(bst.root)

    elif choice == 4:
        break

    else:
        print("Invalid choice")