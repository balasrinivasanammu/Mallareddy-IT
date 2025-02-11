def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):  
        return 3
    return 0

# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():  
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
        else:  
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    
   
    while stack:
        output.append(stack.pop())

    return "".join(output)


expression = "a+b"
postfix = infix_to_postfix(expression)
print("Postfix Expression:", postfix)