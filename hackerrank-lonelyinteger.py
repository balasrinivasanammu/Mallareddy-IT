# Read number of queries (though in this case it's unnecessary for the input format)
n = int(input())

# Read the list of integers
arr = list(map(int, input().split()))

# Use XOR to find the lonely integer
lonely_integer = 0
for num in arr:
    lonely_integer ^= num

# Print the lonely integer
print(lonely_integer)
