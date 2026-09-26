class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, val):
        new_node = Node(val)

        if self.isEmpty():
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def display(self):
        if self.isEmpty():
            print("Linked List is empty...")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print("None")

    def delete(self, val):
        if self.isEmpty():
            print("Nothing to delete...")
            return

        if self.head.data == val:
            self.head = self.head.next
            print("Employee", val, "is deleted...")
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == val:
                prev.next = temp.next
                print("Employee", val, "is deleted...")
                return

            prev = temp
            temp = temp.next

        print("Employee", val, "not found...")


n = LL()

# Creating the given employee list
n.insert("E201")
n.insert("E202")
n.insert("E203")
n.insert("E204")
n.insert("E205")

print("Original Employee List:")
n.display()

print("\nDeleting E201...")
n.delete("E201")

print("\nUpdated Employee List:")
n.display()

print("\nHead now points to:", n.head.data)