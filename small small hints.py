output = [1, 2, 3]
print(*output)  # This prints: 1 2 3

my_list = [10, 200, -30, 40, 50]

for num in reversed(my_list):
    print(num,end=" ")
print()   
a=int(input())
i=0
lines = []
while i<a:
    line = input()
    if line:
        lines.append(line)
        i=i+1
    else:
        break
text = '\n'.join(lines)
print(text)