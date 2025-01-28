
n = int(input())

numbers = list(map(int, input().split()))

for i in numbers:
    if numbers[0]%2==0:
        if i%2!=0:
            print(i,end=" ")
    else:
        if i%2==0:
            print(i,end=" ")
    
    



