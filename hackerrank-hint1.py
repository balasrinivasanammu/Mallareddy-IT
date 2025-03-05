from collections import Counter

def missingNumbers(arr, brr):
    # Count the frequency of each number in both lists using Counter
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    print(count_arr,count_brr)

arr1 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr1 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

missingNumbers(arr1,brr1)
