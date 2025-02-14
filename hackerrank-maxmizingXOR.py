def maximizing_xor(l, r):
    # XOR the two numbers to find where they differ
    xor_result = l ^ r
    
    # Find the most significant bit that is different
    max_xor = 0
    while xor_result > 0:
        max_xor = (max_xor << 1) | 1
        xor_result >>= 1
        
    return max_xor

# Read input values
l = int(input())
r = int(input())

# Compute and print the result
print(maximizing_xor(l, r))
