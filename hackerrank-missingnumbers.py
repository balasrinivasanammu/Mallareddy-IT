def missingNumbers(arr, brr):

    arr_count = {}
    brr_count = {}
    
    for num in arr:
        if num in arr_count:
            arr_count[num] += 1
        else:
            arr_count[num] = 1
    print(arr_count)
    
    for num in brr:
        if num in brr_count:
            brr_count[num] += 1
        else:
            brr_count[num] = 1
    print(brr_count)
 
    missing = []
    for num in brr_count:
        print(brr_count[num])
        if brr_count[num] > arr_count.get(num, 0):
            missing.append(num)
    
    return sorted(missing)


arr1 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr1 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]


print(*missingNumbers(arr1, brr1))  
