def linear_search(arr, target):
   
    for index in range(len(arr)):
        print(f"Checking index {index}, value {arr[index]}")

        if arr[index] == target:
            return index  
    return -1  

# Example usage:
arr = [30, 20, 50, 30,40]
target = 30
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
