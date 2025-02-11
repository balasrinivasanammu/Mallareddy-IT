def generate_parentheses(n):
    result = []
    stack = [("", 0, 0)]  # Stack to store (current_string, open_count, close_count)
    #print(stack.pop())
    while stack:
        #print('stack ',stack)
        current_string, open_count, close_count = stack.pop()
        #print(current_string, open_count, close_count)
        # If we've used n open and n close parentheses, the combination is valid
        if open_count == n and close_count == n:
            result.append(current_string)
            #print("cstring",result)
            continue
        
        # If we can still add an open parenthesis, push it onto the stack
        if open_count < n:
            stack.append((current_string + '(', open_count + 1, close_count))
        
        # If we can still add a close parenthesis (close_count < open_count), push it onto the stack
        if close_count < open_count:
            stack.append((current_string + ')', open_count, close_count + 1))

    return result

# Test the function with n = 2
n = 2
result = generate_parentheses(n)
print(",".join(result))  # Output: ()() (())
