def search_sorted(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid] and nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[low]<=nums[mid]:
            if nums[low]<=target and target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<=target and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False
print(search_sorted([7,8,1,2,3,3,3,4,5,6],3))

