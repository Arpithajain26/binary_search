def smalles_element(nums):
    low=0
    high=len(nums)-1
    ans=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if nums[low]<=nums[high]:
            ans=min(nums[low],ans)
            break
        if (nums[low]<=nums[mid]):
            ans=min(ans,nums[low])
            low=mid+1
        else:
            ans=min(ans,nums[mid])
            high=mid-1
    return ans
print(smalles_element([4,5,6,0,1,2]))