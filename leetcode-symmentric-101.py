from collections import deque

# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build tree from list
def buildTreeFromList(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while i < len(lst):
        current = queue.popleft()
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

# Iterative function to check if tree is symmetric
def isSymmetric(root):
    if not root:
        return True
    
    queue = deque([root.left, root.right])  # Compare left and right children of the root
    
    while queue:
        left = queue.popleft()
        right = queue.popleft()
        
        # If both nodes are None, continue to next pair
        if not left and not right:
            continue
        
        # If one of the nodes is None or values do not match, return False
        if not left or not right or left.val != right.val:
            return False
        
        # Add child nodes in reverse order
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    
    return True

# Get input from user
tree_input = input("Enter the tree in list form (e.g. [1,2,2,3,4,4,3]): ")
tree_input = eval(tree_input)  # Convert input string to list

# Build the tree from input list
root = buildTreeFromList(tree_input)

# Check if the tree is symmetric
result = isSymmetric(root)
print("Output:", result)
