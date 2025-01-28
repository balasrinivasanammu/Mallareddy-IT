
n = int(input())
lst = list(map(int, input().split()))  

lst.sort(key=lambda x: len(str(x)))

print(" ".join(map(str, lst)))

