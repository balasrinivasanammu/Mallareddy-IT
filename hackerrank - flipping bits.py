def flippingBits(n):
    # The maximum value for a 32-bit unsigned integer
    MAX_UINT_32 = 4294967295
   
    return MAX_UINT_32 - n


t = int(input())  
for _ in range(t):
  
    n = int(input())
    
    print(flippingBits(n))
