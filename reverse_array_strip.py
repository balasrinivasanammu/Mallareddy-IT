# Read input
n = int(input().strip())  # First input is the number of elements
arr = list(map(int, input().strip().split()))  # Second input is the list of numbers

# Reverse the array
arr = arr[::-1]

# Print the result
print(" ".join(map(str, arr)))
