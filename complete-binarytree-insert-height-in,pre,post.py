# Define the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Insert a new node in the binary tree
def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.val:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# In-order traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Pre-order traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Post-order traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Calculate the height of the tree
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

# Example usage
root = TreeNode(10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 13)
insert(root, 18)

print("In-order traversal:")
inorder(root)  # Expected output: 3 5 7 10 13 15 18

print("\nPre-order traversal:")
preorder(root)  # Expected output: 10 5 3 7 15 13 18

print("\nPost-order traversal:")
postorder(root)  # Expected output: 3 7 5 13 18 15 10

print("\nHeight of the tree:")
print(height(root))  # Expected output: 3 (The tree has 3 levels)

