MOD = 10**9 + 7

def shortPalindrome(s):
    # Step 1: Initialize the frequency dictionary for each character
    n = len(s)
    freq = {}

    # Step 2: Create a list to count pairs of indices where s[i] == s[l] and s[j] == s[k]
    count_pairs = {}
    count=0
    # Step 3: Traverse the string and count possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # Add this pair as a valid potential palindrome part
                count=count+1
                count_pairs[(i, j)] = count_pairs.get((i, j), 0) + 1
    
    #For printing result 
    #print(count_pairs)
    print(count)


# Test Cases 
shortPalindrome('ghhggh')  # Output
