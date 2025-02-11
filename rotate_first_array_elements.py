# Read input
n = int(input().strip())  
arr = list(map(int, input().split()))

# Rotate the list by shifting the first element to the end
arr = arr[1:] + [arr[0]]

# Print the result
print(" ".join(map(str, arr)))
