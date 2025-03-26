'''Algo:
    v[i,w]=max{v[i-1,w],v[i-1,w-w[i]]+p[i]}
    '''
# Test cases
'''weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

weights = [2,3,5,7,1,4,1]
values = [10,5,15,7,6,18,3]
capacity = 15

weights = [2,3,4,5]
values =  [1,2,5,6]
capacity = 8
'''




def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum value in Knapsack: ", knapsack(weights, values, capacity))