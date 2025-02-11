def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

# Example 1
nums1 = [2, 2, 1]
print(singleNumber(nums1))  # Output: 1

# Example 2
nums2 = [4, 1, 2, 1, 2]
print(singleNumber(nums2))  # Output: 4

# Example 3
nums3 = [1]
print(singleNumber(nums3))  # Output: 1


0 - 0 0 0 0
2 - 0 0 1 0
2 - 0 0 1 0

2 - 0 0 1 0
2 - 0 0 1 0
0 - 0 0 0 0

0 - 0 0 0 0
1 - 0 0 0 1
1 - 0 0 0 1