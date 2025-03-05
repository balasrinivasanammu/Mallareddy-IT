def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
  
    return list(set1 & set2)

# Example 1:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result1 = intersection(nums1, nums2)
print(result1) 

# Example 2:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result2 = intersection(nums1, nums2)
print(result2)  