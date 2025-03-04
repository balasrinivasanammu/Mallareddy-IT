def sumXor(n):
    
    if n < 0:
        return 0
    count = 0
    while n:
        # Check if the lowest bit is zero
        if n & 1 == 0:
            count += 1
        n >>= 1
    return 2 ** count

if __name__ == '__main__':
    n = int(input().strip())
    print(sumXor(n))
