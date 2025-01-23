import time

def print_first_element(arr):
    print(arr[0])

# Measure execution time
start_time = time.time()
arr = [1, 2, 3, 4, 5]
print_first_element(arr)
end_time = time.time()

print(f"Execution Time for O(1): {end_time - start_time} seconds")


import time

def print_all_elements(arr):
    for element in arr:
        print(element)

# Measure execution time
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # You can increase this size to test
start_time = time.time()
print_all_elements(arr)
end_time = time.time()

print(f"Execution Time for O(n): {end_time - start_time} seconds")


import time

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Measure execution time
arr = [1, 2, 3, 4, 5]  # Increase size for larger execution time
start_time = time.time()
print_pairs(arr)
end_time = time.time()

print(f"Execution Time for O(n^2): {end_time - start_time} seconds")
