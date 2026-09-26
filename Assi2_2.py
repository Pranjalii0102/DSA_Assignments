class Queue:
    def __init__(self):
        self.queue = [None] * 100
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxno = 100

    def isFull(self):
        return self.count == self.maxno

    def isEmpty(self):
        return self.count == 0

    def idExists(self, order_id):
        i = self.front
        j = 0

        while j < self.count:
            if self.queue[i] == order_id:
                return True

            i = i + 1

            if i == self.maxno:
                i = 0

            j = j + 1

        return False

    def enqueue(self, order_id):
        if self.isFull():
            print("Queue Overflow. Cannot accept new order.")
            return

        if self.idExists(order_id):
            print("Duplicate Order ID. Order cannot be accepted.")
            return

        confirmed = input("Is the order confirmed? (yes/no): ")

        if confirmed != "yes":
            print("Only confirmed orders are accepted.")
            return

        self.rear = self.rear + 1

        if self.rear == self.maxno:
            self.rear = 0

        self.queue[self.rear] = order_id
        self.count = self.count + 1

        print(order_id, "placed successfully.")

    def dequeue(self):
        if self.isEmpty():
            print("Order Queue is empty. No order to prepare.")
        else:
            prepared = self.queue[self.front]

            self.queue[self.front] = None

            self.front = self.front + 1

            if self.front == self.maxno:
                self.front = 0

            self.count = self.count - 1

            print(prepared, "prepared and removed from the queue.")

    def peek(self):
        if self.isEmpty():
            print("Order Queue is Empty.")
        else:
            print("Next Order to Prepare:", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Order Queue is empty.")
        else:
            print("Order Queue:", end=" ")

            i = self.front
            j = 0

            while j < self.count:
                print(self.queue[i], end=" ")

                i = i + 1

                if i == self.maxno:
                    i = 0

                j = j + 1

            print()


q = Queue()

while True:
    print("\n1. Place Order")
    print("2. Prepare Order")
    print("3. View Next Order")
    print("4. Display Order Queue")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        order_id = input("Enter Order ID: ")
        q.enqueue(order_id)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")