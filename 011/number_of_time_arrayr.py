def number_of_times_array_rotated(nums):
    low = 0
    high = len(nums) - 1
    index = -1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        # If array is already sorted
        if nums[low] <= nums[high]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            break

        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] < ans:
                index = low
                ans = nums[low]
            low = mid + 1

        # Right half sorted
        else:
            if nums[mid] < ans:
                index = mid
                ans = nums[mid]
            high = mid - 1

    return index


nums = [4, 5, 6, 7, 0, 1, 2]
print(number_of_times_array_rotated(nums))