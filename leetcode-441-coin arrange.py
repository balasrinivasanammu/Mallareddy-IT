def arrangeCoins(n):
    k = 0
    while n >= k + 1:
        k += 1
        n -= k
    return k
n=5
print(arrangeCoins(n))

'''
A time complexity of O(√n) means that the number of operations
grows proportionally to the square root of n.
This often occurs in problems involving
progressive summation or factor searching.'''

def is_perfect_square(n):
    for i in range(1, int(n**0.5) + 1):
        if i * i == n:
            return True
    return False

print(is_perfect_square(25))  # Output: True
print(is_perfect_square(26))  # Output: False


