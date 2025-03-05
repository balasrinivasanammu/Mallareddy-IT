'''How the * works in print():

When you pass an iterable (like a list or tuple) to print()
with the * operator, it unpacks the elements of the iterable
and prints them individually. This means instead of printing
the whole list,it will print each element separated
by a space by default.'''

numbers = [1, 2, 3, 4, 5]


print(numbers)  # Output: [1, 2, 3, 4, 5]

# unpack
print(*numbers)  # Output: 1 2 3 4 5




arr_count = {203: 2, 204: 2, 205: 2}


count_203 = arr_count.get(203, 0)
print(count_203)  # Output: 2


count_999 = arr_count.get(999, 0)
print(count_999)  # Output: 0 (default value)

