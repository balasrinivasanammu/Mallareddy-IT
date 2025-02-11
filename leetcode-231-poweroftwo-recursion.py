def isPowerOfTwo(n):
    # Base case: if n is 1, it's a power of 2
    if n == 1:
        return True
    # Base case: if n is less than or equal to 0, or not divisible by 2, it's not a power of 2
    elif n <= 0 or n % 2 != 0:
        return False
    # Recursive case: divide n by 2 and call recursively
    else:
        return isPowerOfTwo(n // 2)

# Test the function with the input n = 1
n = 3
print(isPowerOfTwo(n))  # Output should be True
