from collections import deque

def is_palindrome(s):
    dq = deque(s)
    print(dq)

    while len(dq) > 1:
        #print(dq.popleft(), dq.pop())
        #print(dq)
        #print(len(dq))
        if dq.popleft() != dq.pop():
            return False

    return True

#print(is_palindrome("balaji"))  # Output: False
print(is_palindrome("racecar"))    # Output: True
