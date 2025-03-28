
n = int(input().strip())  
arr = list(map(int, input().split()))  

odd_numbers = [x for x in arr if x % 2 != 0]

# Reverse the list of odd numbers
odd_numbers.reverse()

result = []
odd_index = 0

for num in arr:
    if num % 2 != 0:
        result.append(odd_numbers[odd_index])
        odd_index += 1
    else:
        result.append(num)

# Print the result
print(" ".join(map(str, result)))
