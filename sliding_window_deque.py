from collections import deque

def sliding_window_max(nums, k):
    result = []
    dq = deque()  # stores indices of elements

    for i, num in enumerate(nums):
        # Remove elements that are out of the window
        #print(dq and dq[0] < i - k + 1)
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove all elements smaller than the current element
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Append the maximum element in the window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
