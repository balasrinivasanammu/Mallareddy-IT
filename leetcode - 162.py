def findPeakElement(nums):
    n = len(nums)
    #def findPeakElement(nums):
    #n = len(nums)
    
    # Check if the first element is a peak
    if n == 1 or nums[0] > nums[1]:
        return 0
    
    # Check if the last element is a peak
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    # Check for a peak in the middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    
    return -1  # This is just a fallback, though there should always be a peak.

# Example 1
nums1 = [1, 2, 3, 1]
print(findPeakElement(nums1))  # Output: 2 (Index of peak element 3)

# Example 2
nums2 = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums2))  # Output: 5 (Index of peak element 6)


    # Check if the first element is a peak
    if n == 1 or nums[0] > nums[1]:
        return 0
    
    # Check if the last element is a peak
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    # Check for a peak in the middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    
    return -1  # This is just a fallback, though there should always be a peak.

# Example 1
nums1 = [1, 2, 3, 1]
print(findPeakElement(nums1))  # Output: 2 (Index of peak element 3)

# Example 2
nums2 = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums2))  # Output: 5 (Index of peak element 6)
