class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a node on list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Update a node with new data
    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"Updated {old_data} to {new_data}")
                return
            current = current.next
        print(f"Value {old_data} not found in the list.")

    # Delete a node with specific data
    def delete(self, data):
        current = self.head

        # Case 1: The list is empty
        if not current:
            print("The list is empty. No node to delete.")
            return

        # Case 2: The node to be deleted is the head
        if current.data == data:
            self.head = current.next  # Move head to the next node
            current = None  # Free the memory
            print(f"Node with data {data} deleted.")
            return

        # Case 3: Traverse the list to find the node to delete
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # Case 4: The node with the given data is not found
        if current is None:
            print(f"Node with data {data} not found.")
            return

        # Case 5: Delete the node by adjusting the previous node's next pointer
        prev.next = current.next
        current = None  # Free the memory
        print(f"Node with data {data} deleted.")

    # Search for a node in the list
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"Found {data}")
                return
            current = current.next
        print(f"{data} not found in the list.")

    # Display the list
    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Menu-driven interface
def menu():
    linked_list = SinglyLinkedList()

    while True:
        print("\nSingly Linked List Operations")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Search")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert: "))
            linked_list.insert(data)
        elif choice == 2:
            old_data = int(input("Enter data to update: "))
            new_data = int(input("Enter new data: "))
            linked_list.update(old_data, new_data)
        elif choice == 3:
            data = int(input("Enter data to delete: "))
            linked_list.delete(data)
        elif choice == 4:
            data = int(input("Enter data to search: "))
            linked_list.search(data)
        elif choice == 5:
            linked_list.display()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
