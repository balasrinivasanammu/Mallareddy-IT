class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself to form the circular link
        else:
            current = self.head
            while current.next != self.head:  # Traverse to the last node
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Complete the circular link

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (back to head)")

# Create a circular linked list
cll = CircularLinkedList()

# Input from the user
n = int(input("Enter the number of elements in the circular linked list: "))
for i in range(n):
    data = input(f"Enter data for node {i + 1}: ")
    cll.append(data)

# Display the circular linked list
print("\nThe Circular Linked List is:")
cll.display()