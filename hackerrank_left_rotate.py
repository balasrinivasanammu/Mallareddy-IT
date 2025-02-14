def left_rotate(arr, d):
    n = len(arr)
   
    return arr[d % n:] + arr[:d % n]


n,d = list(map(int,(input().split())))
arr = list(map(int,input().split()))


result = left_rotate(arr, d)


print(" ".join(map(str, result)))

'''

For the array [1, 2, 3, 4, 5] and d = 2:

    d % n = 2 % 5 = 2
    arr[2:] = [3, 4, 5]
    arr[:2] = [1, 2]
    Combining them: [3, 4, 5] + [1, 2] = [3, 4, 5, 1, 2]
    
    '''
