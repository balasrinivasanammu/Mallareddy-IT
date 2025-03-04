class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        new_node = Node(key)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            current = self.table[i]
            if current:
                chain = []
                while current:
                    chain.append(current.key)
                    current = current.next
                print(f"Index {i}: {chain}")
            else:
                print(f"Index {i}: Empty")

# Example usage
hash_table = HashTableChaining(10)
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.display()

print(f"Search for 15: {hash_table.search(15)}")
print(f"Search for 100: {hash_table.search(100)}")
