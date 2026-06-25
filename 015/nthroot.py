def nthroot(n, m):   # n = root, m = number
    low = 1
    high = m
    eps = 1e-6
    
    def multiply(number, n):
        ans = 1.0
        for _ in range(n):
            ans *= number
        return ans
    
    while (high - low) > eps:
        mid = (low + high) / 2
        
        if multiply(mid, n) < m:
            low = mid
        else:
            high = mid
    
    return low

print(nthroot(3, 27))   # ✅ 3rd root of 27