def single_element(nums):
    for i in range(len(nums)):
        """bruteforce approach
        if nums left side should sam eto nums or right side should be same to nums 
        if not then that is resultant we are searching for"""
        if i==0:
            if nums[i+1]!=nums[i]:
                return nums[i]
        elif i==len(nums)-1:
            if nums[i]!=nums[i-1]:
                return nums[i]
        else:
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
print(single_element([1,1,2,2,3,3,4,5,5,6,6,7,7,8,8]))

def single_element1(nums):
    low=0
    high=len(nums)-1
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        if (mid%2!=0 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]) :
            # element left of mid are equal,we need to to eliminate left part
            low=mid+1
        else:
            high=mid-1
    return -1
print(single_element1([1,1,2,2,3,3,4,5,5,6,6]))

        

        



