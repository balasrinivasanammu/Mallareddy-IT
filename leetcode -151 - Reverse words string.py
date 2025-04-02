def reverseWords(s):
    return " ".join(s.split()[::-1])


#s = "  hello   world  "
s = "the sky is blue"
print(reverseWords(s))  