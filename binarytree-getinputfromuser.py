# Define the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Iterative Insert function to insert a new value into the binary tree
def insert(root, value):
    new_node = TreeNode(value)
    
    # If the tree is empty, make the new node the root
    if root is None:
        return new_node
    
    # Start from the root and find the correct position for the new node
    current = root
    while True:
        if value < current.val:
            # Go to the left subtree
            if current.left is None:
                current.left = new_node
                break
            else:
                current = current.left
        else:
            # Go to the right subtree
            if current.right is None:
                current.right = new_node
                break
            else:
                current = current.right
                
    return root

# In-order traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Function to handle user input and tree insertion iteratively
def create_tree():
    root = None
    while True:
        try:
            value = int(input("Enter a number to insert into the tree (or type 'stop' to finish): "))
            root = insert(root, value)
        except ValueError:
            print("Finished inserting values.")
            break
    return root

# Example usage
print("Welcome to the Binary Search Tree insertion program!")

# Create the tree by taking user input
root = create_tree()

# Print the tree (in-order traversal)
print("\nIn-order traversal of the tree:")
inorder(root)  # This will print the values in sorted order
