
n = int(input())
lst = list(map(int, input().split()))  

lst.sort(key=lambda x: len(str(x)))

print(" ".join(map(str, lst)))
'''
print(lst.sort())

syntax of lamba:
    lambda arg: expr
    
    only one expression
    but n no of arg
    
    '''






Sample Input:
    4
    15 1 800 250
Sampl output:
    1 15 800 250
    
    your output
    1 15 250 800

