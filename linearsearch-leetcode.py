def linear_search(arr, target):
    
    for index, value in enumerate(arr):
        if value == target:
            return index  
    return -1  

# Example usage:
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
