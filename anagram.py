def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # If the lengths are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if are_anagrams(str1, str2):
    print("Yes, they are anagrams!")
else:
    print("No, they are not anagrams.")
