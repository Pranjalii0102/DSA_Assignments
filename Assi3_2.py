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
            print("Waiting List is empty...")
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
            print("Passenger", val, "is deleted...")
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == val:
                prev.next = temp.next
                print("Passenger", val, "is deleted...")
                return

            prev = temp
            temp = temp.next

        print("Passenger", val, "not found...")


n = LL()

# Creating the given waiting list
n.insert(201)
n.insert(202)
n.insert(203)

print("Original Railway Waiting List:")
n.display()

# Insert Passenger 204
print("\nInserting Passenger 204...")
n.insert(204)

print("\nWaiting List after inserting 204:")
n.display()

# Delete Passenger 202
print("\nDeleting Passenger 202...")
n.delete(202)

print("\nUpdated Railway Waiting List:")
n.display()