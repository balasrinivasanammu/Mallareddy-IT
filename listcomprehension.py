Syntax: List Comprehension
    
[expression for item in iterable if condition]

expression: This is the value that you want to include in the resulting list.
item: This is the variable representing each element in the iterable.

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)


#-----------------------

# Using list comprehension to get all even numbers between 1 and 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)


#----------------------------

# Using list comprehension to generate squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)


#----------------------------

# Using list comprehension to extract vowels from a string
text = "Hello, how are you?"
vowels = [char for char in text if char.lower() in 'aeiou']
print(vowels)


#----------------------------

words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)


#--------------------------------


numbers = [10, 15, 30, 45, 60, 70, 100]
div_by_3_and_5 = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
print(div_by_3_and_5)


#----------------------------------

words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)


#----------------------------------

words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words)


#-----------------------------------

