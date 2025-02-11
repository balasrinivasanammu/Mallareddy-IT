def nearest_greater_elements(arr):
    stack = []
    result = []  

    for num in reversed(arr):
        
        while stack and stack[-1] <= num:
            stack.pop()

        
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

       
        stack.append(num)

    # Reverse the result list to match the order of the original array
    result.reverse()
    return result
a=int(input())
arr=list(map(int,input().split()))
    
 
output = nearest_greater_elements(arr)

print(*output)
#print(" ".join(map(str,output)))
