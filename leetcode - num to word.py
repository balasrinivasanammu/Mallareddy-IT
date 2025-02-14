def num_to_words(num):
    # Lists for numbers and places
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    thousands = ["", "Thousand", "Million", "Billion", "Trillion"]
    
    # Helper function to convert numbers less than 1000
    def helper(n):
        if n == 0:
            return ""

        elif n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        
        else:
            return ones[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
    
    # If number is 0, return "Zero"
    if num == 0:
        return "Zero"
    
    result = ""
    place = 0
    
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + " " + thousands[place] + " " + result
        num //= 1000
        place += 1
    
    return result.strip()

# Input number
num = int(input())#95

# Convert and print the result
print(num_to_words(num))
