def maximumSum(a, m):
    prefix_sum = 0
    max_mod = 0
    mod_prefix = [0]  
    
    for num in a:
        prefix_sum = (prefix_sum + num) % m  
        
        for prev in mod_prefix:
            max_mod = max(max_mod, (prefix_sum - prev + m) % m)
        
        mod_prefix.append(prefix_sum)
    
    return max_mod

# Reading input
q = int(input())  

for _ in range(q):
    n, m = map(int, input().split())  
    a = list(map(int, input().split()))  
    
    result = maximumSum(a, m)
    print(result)
