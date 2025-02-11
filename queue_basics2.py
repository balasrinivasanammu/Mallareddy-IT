from collections import deque

# Create a deque
dq = deque([1, 2, 3, 4])

# Remove and return the leftmost item (front of the deque)
item = dq.popleft()

print(f"Removed item: {item}")  # Output: Removed item: 1
print(f"Deque after popleft: {dq}")  # Output: Deque after popleft: deque([2, 3, 4])

'''
Hint:
    The time complexity of popleft() is O(1),
    which is much more efficient than using list.pop(0), which has O(n) complexity.
    
    '''