import heapq # priority queue

def kSmallestPairs(nums1, nums2, k): # 1,7,11 ----- 2,4,6------3
    # Check if either list is empty
    if not nums1 or not nums2:
        return []

    # Min-heap
    heap = []
    # Initialize the heap with the first element of nums1 paired with all elements in nums2
    for i in range(min(k, len(nums1))):  # No need to go beyond k elements in nums1
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))  # (sum, i, j) where i is index in nums1 and j in nums2
    print(heap)
    
    result = []
    
    while heap and len(result) < k: # [(3, 0, 0), (9, 1, 0), (13, 2, 0)] and 0<3:
        #print(heap)
        sum_val, i, j = heapq.heappop(heap) # (3,0,0)
        result.append([nums1[i], nums2[j]]) # (1,2)
        #print(len(result))

        # If there's another element in nums2 to pair with nums1[i], push it into the heap
        if j + 1 < len(nums2): # 1<3
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1)) # (1+4),0,1
    
    return result










nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
final=kSmallestPairs(nums1, nums2, k)
print(final)