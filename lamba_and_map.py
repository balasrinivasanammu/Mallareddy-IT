'''
Lambda Function

A lambda function is a small anonymous function defined
with the lambda keyword.
Here's an example of a lambda function that adds two numbers:
'''
# Lambda function to add two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(5, 3)
print(result)  # Output: 8

#map function  - manipulate the values

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda function to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert map object to list and print the result
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


#-------------------------------------

numbers = [1,2,3,4]

# returns the square of a number
def square(number):
  return number * number

# apply square() to each item of the numbers list
squared_numbers = map(square, numbers)

# converting to list for printing
result = list(squared_numbers)
print(result) 

# Output: [1,4,9,16]

#-------------------------------------

def square(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(square, numbers)
#print(result)

# converting the map object to set
result = set(result)
print(result)



# ----------------------- Map with lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# convert to set and print it
print(set(result))

