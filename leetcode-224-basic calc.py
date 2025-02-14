def calculate(s: str) -> int:
    stack = []  
    current_number = 0  
    sign = 1  # 1 for positive, -1 for negative
    result = 0  # The final result
    
    for char in s:
        if char.isdigit():
            # Build the current number (since numbers can be more than 1 digit)
            current_number = current_number * 10 + int(char)
        elif char == '+':
            # Add the current number to the result
            result += sign * current_number
            current_number = 0  # Reset current number
            sign = 1  # Update sign to positive
        elif char == '-':
            # Add the current number to the result with a negative sign
            result += sign * current_number
            current_number = 0  # Reset current number
            sign = -1  # Update sign to negative
        elif char == '(':
            # Push the result and sign onto the stack and reset for a new sub-expression
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Add the current number to the result (considering the sign)
            result += sign * current_number
            current_number = 0  # Reset current number
            # Pop the sign and previous result from the stack
            result *= stack.pop()  # The sign before the parenthesis
            result += stack.pop()  # The result before the parenthesis
    
    # Finally, add the last number to the result
    result += sign * current_number
    return result

# Test Cases
n=input()
print(calculate(n))  # Output: 2
#print(calculate(" 2-1 + 2 "))  # Output: 3
#print(calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
