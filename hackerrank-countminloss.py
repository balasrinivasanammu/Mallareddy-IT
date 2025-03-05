def minimumLoss(prices):
    # Store the minimum loss, initialized to a large number
    min_loss = float('inf')
    
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            
            
            if prices[i] > prices[j]:
               
                loss = prices[i] - prices[j]
               
                
                if loss < min_loss:
                    min_loss = loss
    
    return min_loss


#print(minimumLoss([20, 7, 8, 2, 5]))  
#print(minimumLoss([20, 15, 8, 2, 12])) 

print(minimumLoss([5, 10, 3]))  
