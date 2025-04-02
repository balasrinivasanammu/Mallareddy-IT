def isHappy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Sum of squares of digits
    
    return n == 1

print(isHappy(19))  # Output: True
print(isHappy(2))   # Output: False
