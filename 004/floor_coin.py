def floor(nums,target):
    ans=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=target:
            ans=nums[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
def ceil_element(nums,target):
    ans=-1
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
print(floor([10,20,30,40,50],25))
print(ceil_element([10,20,30,40,50],25))

