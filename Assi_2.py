class Queue:
    def __init__(self):
        self.queue = []
        self.max_size = 5

    def enqueue(self, customer):
        if len(self.queue) == self.max_size:
            print("Queue is full")
        else:
            self.queue = self.queue + [customer]
            print("Customer added successfully")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            customer = self.queue[0]
            self.queue = self.queue[1:]
            print("Removed customer:", customer)

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Customers in queue:")
            for customer in self.queue:
                print(customer)


q = Queue()

while True:
    print("\n1. Add Customer")
    print("2. Remove Customer")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        customer = input("Enter customer name: ")
        q.enqueue(customer)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")