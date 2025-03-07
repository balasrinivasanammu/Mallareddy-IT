def bucket_sort(arr):
    # Step 1: Create an empty list of buckets
    if len(arr) == 0:
        return arr

    # Find the maximum and minimum values in the input array
    min_value = min(arr)
    max_value = max(arr)
    
    # Calculate the range of each bucket (here we divide into 10 buckets)
    bucket_count = len(arr)
    bucket_range = (max_value - min_value) / bucket_count

    # Step 2: Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Distribute elements into the buckets
    for num in arr:
        # Determine the index of the bucket
        index = int((num - min_value) // bucket_range)
        if index == bucket_count:  # To handle edge case when num is exactly the max value
            index -= 1
        buckets[index].append(num)

    # Step 4: Sort each bucket and merge them
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Sort individual buckets and merge
    
    return sorted_arr

# Example usage:
if __name__ == "__main__":
    arr = [0.42, 0.32, 0.53, 0.10, 0.77, 0.63, 0.89, 0.43]
    #arr = [42, 32, 53, 10, 77, 63, 89, 43]
    print("Original array:", arr)
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)
