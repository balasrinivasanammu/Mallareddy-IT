class HashTableBucket:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize each index with an empty list (bucket)

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        print(index)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        print(index)
        return key in self.table[index]

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Example usage
hash_table = HashTableBucket(10)
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.display()

print(f"Search for 15: {hash_table.search(15)}")
print(f"Search for 100: {hash_table.search(100)}")
