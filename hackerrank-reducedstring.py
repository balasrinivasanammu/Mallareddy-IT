def super_reduced_string(s):
    # Using a stack to remove adjacent matching pairs
    stack = []
    
    # Traverse each character in the string
    for char in s:
        # If the stack is not empty and the top of the stack matches the current character, pop it
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Otherwise, push the character onto the stack
            stack.append(char)
    
    # If the stack is empty, return "Empty String", else join the stack to form the result
    return "".join(stack) if stack else "Empty String"

# Sample Input and Output
inputs = [
    "aaabccddd",  # Expected Output: "abd"
    "aa",         # Expected Output: "Empty String"
    "baab"        # Expected Output: "Empty String"
]
n=input()

# Process each input

print(super_reduced_string(n))
