def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0
    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break
    
    return total_value

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum value in Knapsack (Greedy): ", knapsack_greedy(weights, values, capacity))