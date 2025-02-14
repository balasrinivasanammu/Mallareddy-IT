class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert method (iterative approach)
    def insert(self, word):
        new_node = Node(word)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if word < current.word:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
    
    # Search method (iterative approach)
    def search(self, word):
        current = self.root
        while current is not None:
            if word == current.word:
                return True
            elif word < current.word:
                current = current.left
            else:
                current = current.right
        return False

# Input
n = int(input())  
words = [int(input()) for _ in range(n)]  

m = int(input())  
queries = [int(input()) for _ in range(m)]  


bst = BST()
for word in words:
    bst.insert(word)
for query in queries:
    if bst.search(query):
        print(f"{query} is there")
    else:
        print(f"{query} is not there")
