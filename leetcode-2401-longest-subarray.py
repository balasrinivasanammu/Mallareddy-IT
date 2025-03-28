def longestNiceSubarray(nums):
    left = 0
    current = 0  
    result = 0

    for right in range(len(nums)):
        
        while current & nums[right] != 0:
            current ^= nums[left]
            left += 1
        
        
        current |= nums[right]
        
        
        result = max(result, right - left + 1)
    
    return result

nums = [1,3,8,48,10]
print(longestNiceSubarray(nums))
