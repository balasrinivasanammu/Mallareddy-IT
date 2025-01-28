# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to compare two linked lists
def are_equal(list1, list2):
    while list1 is not None and list2 is not None:
        if list1.data != list2.data:
            return False
        list1 = list1.next
        list2 = list2.next
    
    # If both lists end at the same time, they're equal
    return list1 is None and list2 is None

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Example usage
list1 = create_linked_list([1, 2, 3, 4])
list2 = create_linked_list([1, 2, 3, 4])
list3 = create_linked_list([1, 2, 3, 5])

# Check if the linked lists are equal
print(are_equal(list1, list2))  # Output: True
print(are_equal(list1, list3))  # Output: False
