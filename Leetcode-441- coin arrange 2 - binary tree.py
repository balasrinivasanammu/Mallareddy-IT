def arrangeCoins(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        sum_mid = (mid * (mid + 1)) // 2
        if sum_mid == n:
            return mid
        elif sum_mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return right  # Right holds the last valid value of mid
n=2
print(arrangeCoins(n))