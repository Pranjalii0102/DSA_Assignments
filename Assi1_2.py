class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.maxno = 15

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxno

    def validName(self, name):
        if name == "":
            return False

        ch = name[0]

        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            return True
        else:
            return False

    def recursiveLevel(self, name):
        level = 0
        temp = self.top

        while temp is not None:
            if temp.data == name:
                level += 1
            else:
                break

            temp = temp.next

        return level

    def push(self, data):
        if self.isFull():
            print("Stack Overflow")
        elif not self.validName(data):
            print("Invalid function name")
        elif self.recursiveLevel(data) >= 3:
            print("Recursive call limit reached")
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.count += 1

            print(data, "called successfully")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            popped = self.top.data

            self.top = self.top.next
            self.count -= 1

            print(popped, "returned successfully")

    def peek(self):
        if self.isEmpty():
            print("Call stack is empty")
        else:
            print("Current Function:", self.top.data)

    def display(self):
        if self.isEmpty():
            print("Call stack is empty")
        else:
            temp = self.top

            print("Call Stack:", end=" ")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


stack = Stack()

while True:
    print("\n1. Call Function")
    print("2. Return from Function")
    print("3. Current Function")
    print("4. Display Call Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        function_name = input("Enter function name: ")
        stack.push(function_name)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")