def count_pairs_with_difference(arr, k):
   
    seen = set()
    pair_count = 0
    
    for num in arr:
        
        if num - k in seen:
            pair_count += 1
        
        
        if num + k in seen:
            pair_count += 1
        
       
        seen.add(num)
    
    return pair_count

# Input
n, k = 5, 2
arr = [1, 5, 3, 4, 2]


print(count_pairs_with_difference(arr, k))  
