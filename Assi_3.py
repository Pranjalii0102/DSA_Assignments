class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Book inserted at beginning")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Book inserted at end")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Deleted book:", self.head.data)
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


l = LinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = input("Enter book name: ")
        l.insert_beginning(data)

    elif choice == 2:
        data = input("Enter book name: ")
        l.insert_end(data)

    elif choice == 3:
        l.delete_beginning()

    elif choice == 4:
        l.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")