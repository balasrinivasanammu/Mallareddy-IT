class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0
    
    total = 0
    
    # Check if left child is a leaf
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    
    # Recursively go to the left and right children
    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    
    return total

# Example usage:
# Construct the binary tree from the input
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Call the function
print(sumOfLeftLeaves(root))  # Output: 24
