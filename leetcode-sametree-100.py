class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def isSameTree(p, q):
    if not p and not q:
        return True
   
    if not p or not q:
        return False
    
   
    queue = [(p, q)]  # Pairing nodes from both trees
    
    while queue:
        node1, node2 = queue.pop(0)
        
        # If the values of the nodes do not match, return False
        if node1.val != node2.val:
            return False
        
        # Add the children of both nodes to the queue to compare them
        if node1.left and node2.left:
            queue.append((node1.left, node2.left))
        elif node1.left or node2.left:  # One is None, the other is not
            return False
        
        if node1.right and node2.right:
            queue.append((node1.right, node2.right))
        elif node1.right or node2.right:  # One is None, the other is not
            return False
    
    return True

# Get input from user
p_input = input("Enter tree p in list form (e.g. [1,2,3]): ")
q_input = input("Enter tree q in list form (e.g. [1,2,3]): ")


p_input = eval(p_input)
q_input = eval(q_input)


p_root = buildTreeFromList(p_input)
q_root = buildTreeFromList(q_input)

result = isSameTree(p_root, q_root)
print("Output:", result)
