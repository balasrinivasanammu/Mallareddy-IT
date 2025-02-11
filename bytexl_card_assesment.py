def cards(n, k, powers):
    deck = []
    
    for power in powers:
        while deck and deck[-1] < power:
            deck.pop()
        deck.append(power)
    
    
    result = len(deck)
    
    return result

# Sample Input
n, k = 6, 2
powers = [1, 6, 9, 5, 3, 10]

# Output the result
print(cards(n, k, powers))