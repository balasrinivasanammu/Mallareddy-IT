def counting_sort(arr, exp):
    # Create a count array to store the count of occurrences of digits (0 to 9)
    count = [0] * 10
    output = [0] * len(arr)

    # Count occurrences of digits in the given exp place (ones, tens, etc.)
    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10] += 1
    

    # Update count[i] to store the actual position of the digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count positions
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_value = max(arr)

    # Perform counting sort for every digit. The exp is 10^i where i is the current digit number
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)
