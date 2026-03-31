def squareroot(num):
    ans=0
    for i in range(num):
        if (i*i<=num):
            ans=i
        else:
            break
    return ans
print(squareroot(28))
def squareroot1(num):
    low=1
    high=num
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(squareroot1(28))
