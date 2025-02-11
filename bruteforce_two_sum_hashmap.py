def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Example usage:
nums = list(map(int,input().split()))
target = int(input())
result = two_sum_bruteforce(nums, target)
print(result)  # Output: [0, 1]







def two_sum_hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return None

# Example usage:
nums = list(map(int,input().split()))
target = int(input())
result = two_sum_hashmap(nums, target)
print(result)  # Output: [0, 1]
