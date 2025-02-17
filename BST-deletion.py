class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def delete_node(self, key):
        node = self.root
        parent = None

        # Step 1: Search for the node to delete
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        # If node not found
        if not node:
            print("Node not found!")
            return

        # Step 2: Node to be deleted has no children (leaf node)
        if node.left is None and node.right is None:
            if parent is None:  # If the tree has only one node
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None

        # Step 3: Node to be deleted has one child
        elif node.left is None:
            if parent is None:
                self.root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right

        elif node.right is None:
            if parent is None:
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        # Step 4: Node to be deleted has two children
        else:
            # Find the in-order successor (smallest in the right subtree)
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace node's value with successor's value
            node.val = successor.val

            # Remove the successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def inorder_traversal(self):
        result = []
        stack = []
        node = self.root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

# Example usage
tree = BST()
tree.root = Node(50)
tree.root.left = Node(30)
tree.root.right = Node(70)
tree.root.left.left = Node(20)
tree.root.left.right = Node(40)
tree.root.right.left = Node(60)
tree.root.right.right = Node(80)

# Delete a node with value 70
tree.delete_node(70)

# In-order traversal of the tree after deletion
print(tree.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 80]
