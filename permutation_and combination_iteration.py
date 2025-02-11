# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
  #  print(result)
    return result

# Function to calculate permutation P(n, r)
def permutation(n, r):
    
    return factorial(n) // factorial(n - r)

# Function to calculate combination C(n, r)
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage:
n = 5  # Total items
r = 3  # Items to choose

# Calculating Permutation P(n, r)
#perm_result = permutation(n, r)
#print(f"Permutation P({n}, {r}) = {perm_result}")
print(permutation(n, r))
print(combination(n, r))
# Calculating Combination C(n, r)
#comb_result = combination(n, r)
#print(f"Combination C({n}, {r}) = {comb_result}")
