# Max-Heap data structure in Python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    array.append(newNum)
    current = len(array) - 1
    while current > 0:
        parent = (current - 1) // 2
        if array[current] > array[parent]:
            array[current], array[parent] = array[parent], array[current]
            current = parent
        else:
            break

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(size):
        if array[i] == num:
            break

    
    array[i], array[-1] = array[-1], array[i]
    array.pop()  # Remove the last element which is now the number to be deleted

    
    if i < len(array):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array:", arr)

deleteNode(arr, 4)
print("After deleting an element:", arr)

