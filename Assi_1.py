class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 5

    def push(self, book):
        if len(self.stack) == self.max_size:
            print("Stack is full")
        else:
            self.stack = self.stack + [book]
            print("Book added successfully")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            book = self.stack[-1]
            self.stack = self.stack[:-1]
            print("Removed book:", book)

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Books in stack:")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])


s = Stack()

while True:
    print("\n1. Add Returned Book")
    print("2. Remove Book")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        s.push(book)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")