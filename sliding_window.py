def s_window_max(nums, k):
    result = []
    
    if not nums or k == 0:
        return result

    for i in range(len(nums) - k + 1):
        # Extract the current window (subarray of size k)
        #print(len(nums) - k + 1)
        window = nums[i:i+k]

        window_max = max(window)

        result.append(window_max)

    return result



# Test case
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(s_window_max(nums, k))  


#Test case :
nums = [10, 20, -10, -30, 50]
k = 3
print(s_window_max(nums, k))


#Test case :
nums = [50,50,50,]
k = 3
print(s_window_max(nums, k))
