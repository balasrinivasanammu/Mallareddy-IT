def selection_sort(arr):
    n = len(arr)#3
    for i in range(n):#0,1,2,3
        min_index = i  # 0,1,2 
        for j in range(i+1, n): #1,2,3----2,3----3
            if arr[j] < arr[min_index]:#35<65,25<35--- 65<35
                min_index = j  #  1, 2 
        arr[i], arr[min_index] = arr[min_index], arr[i]#25,35,65


arr = [65, 35, 25]
selection_sort(arr)
print("Sorted array:", arr)
