class Node:
    def __init__(self,box_id,weight,fragile):
        self.box_id=box_id
        self.weight=weight
        self.fragile=fragile
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.count=0
        self.maxno=40

    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count==self.maxno

    def idExists(self,box_id):
        temp=self.top

        while temp is not None:
            if temp.box_id==box_id:
                return True
            temp=temp.next

        return False

    def push(self,box_id,weight,fragile):
        if self.isFull():
            print("Stack overflow")
            return

        if weight<1 or weight>50:
            print("Invalid weight. Weight must be between 1kg and 50kg")
            return

        if fragile and weight>20:
            print("Fragile box weighing more than 20kg cannot be stored")
            return

        if self.idExists(box_id):
            print("Box ID already exists")
            return

        new_node=Node(box_id,weight,fragile)
        new_node.next=self.top
        self.top=new_node
        self.count+=1

        print(box_id, "stored in warehouse")

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            removed=self.top

            print(removed.box_id, " removed from warehouse")
            print("Weight : ",removed.weight,"kg")

            self.top=self.top.next
            self.count-=1

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top Box ID : ", self.top.box_id)
            print("Weight :", self.top.weight, "kg")


            if self.top.fragile:
                print("Fragile : Yes")
            else:
                print("Fragile : NO")

    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp=self.top

            print("Box Stack :")

            while temp is not None:
                print("Box ID :", temp.box_id, "| Weight :", temp.weight,"kg", "| Fragile :", temp.fragile)

                temp=temp.next

stack=Stack()

while True:
    print("\n1. Store Box")
    print("2. Remove Box")
    print("3. Top Box")
    print("4. Display Box Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        box_id = input("Enter Box ID: ")
        weight = float(input("Enter weight of box: "))

        f = input("Is the box fragile? (yes/no): ")

        if f == "yes":
            fragile = True
        else:
            fragile = False

        stack.push(box_id, weight, fragile)

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

