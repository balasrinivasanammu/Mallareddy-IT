def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n * factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Test the function
n = 1000000
print(f"The factor of {n} is {factorial(n)}")

'''

5* (5-1) = 20
4* (4-1) = 12
3* (3-1) = 6
2* (2-1) = 2
1* (1-1) = 0

'''
