class Queue:
    def __init__(self):
        self.queue = [None] * 50
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxno = 50

    def isFull(self):
        return self.count == self.maxno

    def isEmpty(self):
        return self.count == 0

    def idExists(self, ticket_id):
        i = self.front
        j = 0

        while j < self.count:
            if self.queue[i] == ticket_id:
                return True

            i = i + 1

            if i == self.maxno:
                i = 0

            j = j + 1

        return False

    def enqueue(self, ticket_id):
        if self.isFull():
            print("Queue is Full. No new passenger can enter.")
            return

        if self.idExists(ticket_id):
            print("Duplicate Ticket ID. Passenger cannot enter.")
            return

        confirmed = input("Is the passenger confirmed? (yes/no): ")

        if confirmed != "yes":
            print("Only confirmed passengers can join the queue.")
            return

        self.rear = self.rear + 1

        if self.rear == self.maxno:
            self.rear = 0

        self.queue[self.rear] = ticket_id
        self.count = self.count + 1

        print(ticket_id, "added to Queue.")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot serve passenger.")
        else:
            removed = self.queue[self.front]

            self.queue[self.front] = None

            self.front = self.front + 1

            if self.front == self.maxno:
                self.front = 0

            self.count = self.count - 1

            print(removed, "served and removed from the queue.")

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
        else:
            print("First Passenger Ticket ID:", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Passenger Queue:", end=" ")

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
    print("\n1. Add Passenger")
    print("2. Serve Passenger")
    print("3. View First Passenger")
    print("4. Display Passenger Queue")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        ticket_id = input("Enter Ticket ID: ")
        q.enqueue(ticket_id)

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