def sqrt_number(num):
    ans=0
    for i in range(1,num+1):
        if i*i<=num:
            ans=i
    return ans
print(sqrt_number(28))
def sqrt_number(num):
    low=1
    high=num
    mid=(low+high)/2
    ans=1
    while(low<=high):
        mid=(low+high)//2
        if mid*mid<=num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(sqrt_number(28))
