def knapsack_greedy(weights, values, capacity):
    
    items = []
    for i in range(len(weights)):
        items.append((values[i], weights[i], values[i] / weights[i]))  # (value, weight, ratio)
    print(items)
   
    def sort_key(item):
        print(item[2])
        return item[2]  # Sorting by ratio (value/weight)
    
    items.sort(reverse=True, key=sort_key)
    print(items)
    total_value = 0
    knapsack = []

    for value, weight, _ in items:
        print(weight)
        if capacity >= weight:
            knapsack.append((value, weight))  
            total_value += value
            capacity -= weight

    return total_value, knapsack

# Example usage
'''weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
'''
'''
weights = [1,2,5,6]
values = [2,3,4,5]
capacity = 8
'''
weights = [2,3,4,5]
values =  [1,2,5,6]
capacity = 8

max_value, chosen_items = knapsack_greedy(weights, values, capacity)
print("Maximum Value:", max_value)
print("Chosen Items (value, weight):", chosen_items)
