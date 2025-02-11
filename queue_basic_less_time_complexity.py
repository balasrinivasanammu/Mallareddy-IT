'''The time complexity for both append and pop operations
using deque is O(1), which is optimal for a queue.'''

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
