def search_rotated_array(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        
    return 

print(search_rotated_array([4,5,6,7,0,1,2],0))
"""another method"""
def search_rotated_array(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        if nums[low]<=nums[mid]:
            if target>=nums[low] and target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target>=nums[mid] and target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
print(search_rotated_array([4,5,6,7,0,1,2],1))
