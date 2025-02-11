'''
Tracking the position in the loop:
In many algorithms (like those involving sliding windows, or
when the index has a specific role in computation), enumerate()
helps keep track of where you are in the sequence.

'''


nums = [10, 20, 30, 40]

for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")


'''

i: The index of the current element in the iterable.
num: The value of the current element in the iterable.

Start from a specific index: By default, enumerate() starts from index 0.
However, you can specify a different
starting index by passing a second argument to enumerate(start=...).

'''
nums = [10, 20, 30, 40]

for i, num in enumerate(nums, start=1):
    print(f"Index: {i}, Value: {num}")
