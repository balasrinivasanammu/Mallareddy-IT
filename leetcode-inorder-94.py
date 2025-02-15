# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build the tree from a list
def buildTreeFromList(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1 
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

# Inorder Traversal function
def inorderTraversal(root):
    result = []
    stack = []
    current = root  
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right     
    return result

tree_input = input()
tree_input = eval(tree_input)  
root = buildTreeFromList(tree_input)
result = inorderTraversal(root)
print(result)
