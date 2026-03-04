def occurences(nums,target):
    count=0
    for i in nums:
        if i==target:
            count+=1
    return count
print(occurences([1,2,2,2,3,4,4],2))
    