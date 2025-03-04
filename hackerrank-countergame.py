def counterGame(n):   
    turn = 0  # 0 for Louise, 1 for Richard   
    while n > 1:
        
        power_of_2 = 1 << (n.bit_length() - 1)
        
        if n == power_of_2:
            n //= 2           
        else:           
            n -= power_of_2       
        turn = 1 - turn       
    return "Richard" if turn == 0 else "Louise"

t = int(input())
for _ in range(t):
    n = int(input())
    print(counterGame(n))
