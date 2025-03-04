class HashTableQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        i = 1

        # Quadratic Probing: find next empty slot
        while self.table[index] is not None:
            index = (index + i**2) % self.size
            i += 1
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        i = 1

        # Quadratic Probing: check each slot
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + i**2) % self.size
            i += 1
        return None  # Key not found

    def display(self):
        print(self.table)

# Example usage
hash_table = HashTableQuadraticProbing(10)
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.display()

print(f"Search for 15: {hash_table.search(15)}")
