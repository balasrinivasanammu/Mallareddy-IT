class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key is not found in the list
        if not current:
            print(f"Node with value {key} not found.")
            return

        # Unlink the node from the list
        prev.next = current.next
        current = None

    # Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    llist = SinglyLinkedList()
    
    # Insert nodes at the beginning
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(20)
    llist.insert_at_beginning(30)
    
    print("Linked list after inserting nodes at the beginning:")
    llist.print_list()
    
    # Delete a node
    print("\nDeleting node with value 20:")
    llist.delete_node(20)
    
    llist.print_list()
    
    # Attempt to delete a node not in the list
    print("\nAttempting to delete node with value 100:")
    llist.delete_node(100)
