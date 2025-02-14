def lca(root, n1, n2):
    if root is None:
        return None
    
    if root.value > n1 and root.value > n2:
        return lca(root.left, n1, n2)
    
    if root.value < n1 and root.value < n2:
        return lca(root.right, n1, n2)
    
    return root

# Example usage
root = Node(20)
insert(root, 10)
insert(root, 30)
insert(root, 5)
insert(root, 15)

ancestor = lca(root, 5, 15)
print(ancestor.value)  # Output: 10
