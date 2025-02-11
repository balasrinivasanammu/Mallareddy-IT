import math

# Function to calculate permutation P(n, r)
def permutation(n, r):
    return math.perm(n, r)

# Function to calculate combination C(n, r)
def combination(n, r):
    return math.comb(n, r)

# Example usage:
n = 5  # Total items
r = 3  # Items to choose

# Calculating Permutation P(n, r)
perm_result = permutation(n, r)
print(f"Permutation P({n}, {r}) = {perm_result}")

# Calculating Combination C(n, r)
comb_result = combination(n, r)
print(f"Combination C({n}, {r}) = {comb_result}")
