def merge_sort(arr):
    
    sublist_size = 1
    n = len(arr)
    
    while sublist_size < n:
        left_index = 0
      
        while left_index < n - sublist_size:
            
            right_index = min(left_index + 2 * sublist_size - 1, n - 1)
            
           
            mid_index = (left_index + right_index) // 2
            
           
            merge(arr, left_index, mid_index, right_index)
            
            
            left_index += 2 * sublist_size
        
        sublist_size *= 2

def merge(arr, left_index, mid_index, right_index):
    
    left_sublist = arr[left_index:mid_index + 1]
    right_sublist = arr[mid_index + 1:right_index + 1]
    
    left_pointer = 0
    right_pointer = 0
    merge_pointer = left_index
    
    
    while left_pointer < len(left_sublist) and right_pointer < len(right_sublist):
        if left_sublist[left_pointer] <= right_sublist[right_pointer]:
            arr[merge_pointer] = left_sublist[left_pointer]
            left_pointer += 1
        else:
            arr[merge_pointer] = right_sublist[right_pointer]
            right_pointer += 1
        merge_pointer += 1
    
    while left_pointer < len(left_sublist):
        arr[merge_pointer] = left_sublist[left_pointer]
        left_pointer += 1
        merge_pointer += 1
    
    while right_pointer < len(right_sublist):
        arr[merge_pointer] = right_sublist[right_pointer]
        right_pointer += 1
        merge_pointer += 1

# Example usage:
arr = [65, 35, 25]
merge_sort(arr)
print("Sorted array:", arr)
