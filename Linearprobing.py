class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)

        # Linear Probing: find next empty slot
        while self.table[index] is not None:
            index = (index + 1) % self.size
            print(index)
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)

        # Linear Probing: check each slot
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
        return None  # Key not found

    def display(self):
        print(self.table)

# Example usage
hash_table = HashTableLinearProbing(10)
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.display()

print(f"Search for 15: {hash_table.search(15)}")
