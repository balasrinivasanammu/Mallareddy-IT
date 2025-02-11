# 1. Queue Implementation (FIFO)

from collections import deque

# Queue implementation
queue = deque()

# Enqueue (add to the back)
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue (remove from the front)
print(queue.popleft())  # Output: 1
print(queue.popleft())  # Output: 2



# 2. Stack Implementation (LIFO)

from collections import deque

# Stack implementation
stack = deque()

# Push (add to the back)
stack.append(1)
stack.append(2)
stack.append(3)

# Pop (remove from the back)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
