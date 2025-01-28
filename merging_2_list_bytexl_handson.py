n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

merged_list = []

for i in range(n):
    merged_list.append(list1[i])
    merged_list.append(list2[n-1-i])

print(" ".join(map(str, merged_list)))
