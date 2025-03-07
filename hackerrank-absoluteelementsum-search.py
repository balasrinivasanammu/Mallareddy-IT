def playingWithNumbers(arr, queries):
    result = []
    shift = 0  

    # Iterate through each query
    for query in queries:
        shift += query 
        abs_sum = sum(abs(x + shift) for x in arr)
        result.append(abs_sum)  
    return result

# Example usage:

# Input
arr = [-1, 2, -3]  # Initial array
queries = [1, -2, 3]  # List of queries

result = playingWithNumbers(arr, queries)

# Output the result
print(*result,sep="\n")  # Output: [5, 7, 6]
