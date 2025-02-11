class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

        
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def is_balanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False




# Example usage
root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(height(root))  # Output: 3


# Example usage
print(is_balanced(root))  # Output: True or False based on the structure of your tree