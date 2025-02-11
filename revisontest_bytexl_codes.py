count = {}
inputs = []
a=int(input())
i=0
while i<a:
    line = input()
    if line:
        inputs.append(line)
        i=i+1
    else:
        break
text = '\n'.join(inputs)    
for item in inputs:
    if item in count:
        count[item] += 1
        print(f"{item}{count[item]}")
    else:
        count[item] = 0
        print("WELCOME")
