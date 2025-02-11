def maxProduct(nums):
    # Sort the array
    nums.sort()
    # Calculate the product of the last two elements
    return (nums[-2] - 1) * (nums[-1] - 1)

# Test the function with the provided input
#nums = [3, 4, 5, 2]
#nums = [1,5,4,5]
nums = [3,7]
print(maxProduct(nums))  # Output should be 12
