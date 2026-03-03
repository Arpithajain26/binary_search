def first_last_occurence(nums,x):
    first=-1
    last=-1
    for i in range(len(nums)):
        if nums[i]==x:
            if first==-1:
                first=i
            last=i
    return [first,last]
print(first_last_occurence([2,4,6,8,8,8,11,13],8))
