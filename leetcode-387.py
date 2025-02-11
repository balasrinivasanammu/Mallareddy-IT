from collections import deque, Counter

def firstUniqChar(s):
    # Create a queue to store characters in the order they appear
    queue = deque(s)
    print(queue)
    
    # Create a Counter to count occurrences of each character
    count = Counter(s)
    print(count)
    
 # Traverse the string
    for char in s:
        count[char] += 1
        queue.append(char)
    
    # Now find the first character in the queue that has a count of 1
    while queue:
        char = queue.popleft()
        if count[char] == 1:
            return s.index(char)  # Return the index of the first non-repeating character
    
    return -1  # If no non-repeating character is found

# Example 1:
s1 = "leetcode"
print(firstUniqChar(s1))  # Output: 0





#----------------

from collections import Counter

def firstUniqChar(s):
    # Count the occurrences of each character in the string - find the fre of char
    count = Counter(s)
    print(count)
    
    # Iterate through the string to find the first character with a count of 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i  # Return the index of the first unique character
    
    return -1  # Return -1 if no unique character is found

# Example 1:
s1 = "leetcode"
print(firstUniqChar(s1))  # Output: 0

