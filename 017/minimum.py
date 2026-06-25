def minimum_blloming(nums, day, m, k):
    if m * k > len(nums):
        return -1

    count = 0
    boque = 0   # ❗ you forgot to initialize this

    for i in range(len(nums)):
        if nums[i] <= day:
            count += 1
        else:
            boque += (count // k)   # ❗ use // not /
            count = 0

    boque += (count // k)   # ❗ last segment

    if boque >= m:
        return True   # ❗ return boolean (important)
    else:
        return False
def solve(nums, m, k):
    low = min(nums)
    high = max(nums)

    while low <= high:
        mid = (low + high) // 2

        if minimum_blloming(nums, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1

    return low


print(solve([7,7,7,7,13,11,12,7], 2, 3))
    


        
