Asymptotic notation is a way of describing the efficiency of algorithms in terms of their input size. The most common asymptotic notations are:

    Big O (O): Describes an upper bound, representing the worst-case scenario.
    Big Omega (Ω): Describes a lower bound, representing the best-case scenario.
    Big Theta (Θ): Describes both the upper and lower bounds, representing the average case.

Example 1: Constant Time - O(1)

def print_first_element(arr):
    print(arr[0])

# Time complexity is O(1)


Example 2: Linear Time - O(n)

def print_all_elements(arr):
    for element in arr:
        print(element)

# Time complexity is O(n), where n is the length of the array


Example 3: Quadratic Time - O(n^2)

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Time complexity is O(n^2), where n is the length of the array

Example 4: Logarithmic Time - O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Time complexity is O(log n), where n is the length of the array

Asymptotic notation is a way of describing the efficiency of algorithms in terms of their input size. The most common asymptotic notations are:

    Big O (O): Describes an upper bound, representing the worst-case scenario.
    Big Omega (Ω): Describes a lower bound, representing the best-case scenario.
    Big Theta (Θ): Describes both the upper and lower bounds, representing the average case.

Let's go through a few simple Python programs and analyze their time complexity using asymptotic notation.
Example 1: Constant Time - O(1)

This function has constant time complexity because the time it takes to execute doesn't depend on the input size.

def print_first_element(arr):
    print(arr[0])

# Time complexity is O(1)

Example 2: Linear Time - O(n)

This function loops through all the elements of the input array once, making the time complexity linear in the size of the array.

def print_all_elements(arr):
    for element in arr:
        print(element)

# Time complexity is O(n), where n is the length of the array

Example 3: Quadratic Time - O(n^2)

This function has quadratic time complexity because it contains a nested loop, meaning the time it takes grows proportionally to the square of the input size.

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Time complexity is O(n^2), where n is the length of the array

Example 4: Logarithmic Time - O(log n)

This function performs binary search, which has a logarithmic time complexity. The input size decreases by half with each step.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Time complexity is O(log n), where n is the length of the array

Example 5: Linearithmic Time - O(n log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# Time complexity is O(n log n), where n is the length of the array
