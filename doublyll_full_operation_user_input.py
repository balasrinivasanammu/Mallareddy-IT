class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

    # Delete a node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:  # Update head if needed
                    self.head = temp.next
                temp = None
                print(f"Deleted {value}")
                return
            temp = temp.next
        print(f"{value} not found in the list.")

# Main program
def main():
    dll = DoublyLinkedList()
    while True:
        print("\nDoubly Linked List Operations")
        print("1. Append (Insert) a value")
        print("2. Delete a value")
        print("3. Display list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            dll.append(value)
        elif choice == '2':
            value = int(input("Enter value to delete: "))
            dll.delete(value)
        elif choice == '3':
            dll.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
