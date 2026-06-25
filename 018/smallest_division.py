import math
def smallest(nums,threshold):
    for d in range(1,max(nums)+1):
        sum=0
        for i in range(len(nums)):
            sum+=math.ceil(nums[i]/d)
        if (sum<=threshold):
            return d
    return -1
print(smallest([1,2,5,9],6))
import math

def sumofd(arr, d):
    total = 0
    for i in range(len(arr)):
        total += math.ceil(arr[i] / d)
    return total

def smallest(arr, threshold):
    low = 1
    high = max(arr)
    
    while low <= high:
        mid = (low + high) // 2
        
        if sumofd(arr, mid) <= threshold:
            high = mid - 1
        else:
            low = mid + 1
            
    return low

print(smallest([1,2,5,9], 6))
    
