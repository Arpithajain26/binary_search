def lower_bound(arr,target):
    ans=len(arr)
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(lower_bound([1,2,3,4,5,6,7,8],5))

