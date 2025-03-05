def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return 0  

# Example usage
nums = [1, 3, 4, 2, 20,30,200]
result = find_duplicate(nums)
print(result)
