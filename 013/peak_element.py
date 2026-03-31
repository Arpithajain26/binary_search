def peak_element(nums):
    for i in range(len(nums)):
        if (i==0 or nums[i-1]<nums[i]) and (i==len(nums)-1 or nums[i]>nums[i+1]):
            return nums[i]
print(peak_element([1,2,3,4,5,6,7,8,5,1]))
def peak_element1(nums):
    if nums[0]>nums[1]:
        return nums[0]
    n=len(nums)
    if nums[n-1]>nums[n-2]:
        return n-1
    low=0
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
            return mid
        elif (nums[mid]>nums[mid-1]):
            low=mid+1
        elif (nums[mid]>nums[mid+1]):
            high=mid-1
    return -1
print(peak_element1([1,2,3,4,5,6,7,8,5,1]))
