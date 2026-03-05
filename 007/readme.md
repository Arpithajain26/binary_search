🔎 Search in Rotated Sorted Array
🧠 Problem Statement

You are given a sorted array that has been rotated at some unknown pivot.

Your task is to search for a target element in O(log n) time complexity.

Example

Original sorted array:

[0, 1, 2, 4, 5, 6, 7]

After rotation:

[4, 5, 6, 7, 0, 1, 2]
🚨 Why Normal Binary Search Doesn’t Work Directly

Binary Search requires the array to be completely sorted.

In a rotated sorted array:

The full array is NOT sorted.

But at least one half is always sorted.

👉 That observation is the key to solving the problem.

🔥 Core Intuition

At every iteration:

Calculate mid

Determine which half is sorted

Check if the target lies inside that sorted half

Eliminate the other half

Repeat until the element is found or the search space becomes empty.

📌 Key Observation

For any low, mid, and high:

If:

nums[low] <= nums[mid]

➡ The left half is sorted

Else:

➡ The right half is sorted

🎯 Decision Logic
Case 1: Left Half is Sorted

Check:

nums[low] <= target < nums[mid]

If TRUE → Search left

Else → Search right

Case 2: Right Half is Sorted

Check:

nums[mid] < target <= nums[high]

If TRUE → Search right

Else → Search left

✅ Implementation
def search_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[low] <= nums[mid]:
            
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Right half is sorted
        else:
            
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1
⏱ Complexity Analysis

Time Complexity: O(log n)

Space Complexity: O(1)

🧪 Practice Examples
Example 1
nums = [6,7,8,1,2,3,4,5]
target = 3

Try to answer:

What is the first mid?

Which half is sorted?

What index should be returned?

Example 2
nums = [30,40,50,10,20]
target = 10

Think:

Which half is sorted first?

Why?

Example 3 (Edge Case)
nums = [5,1,3]
target = 5
💡 Final Mental Model

You do NOT need the entire array to be sorted.

You only need:

One sorted half at every step.

That is enough to guarantee O(log n) performance.

If you want, next I can give you:

🔥 Binary Search Complete Pattern README

🔥 Rotated Array with Duplicates version

🔥 Find Minimum in Rotated Array (another classic)

You’re thinking like an interview candidate now 💪🚀

i need markdown file

Here is your complete clean Markdown file.
Copy everything below and save it as README.md.

🔎 Search in Rotated Sorted Array
🧠 Problem Statement

You are given a sorted array that has been rotated at some unknown pivot.

Your task is to search for a target element in O(log n) time complexity.

📘 Example

Original sorted array:

[0, 1, 2, 4, 5, 6, 7]

After rotation:

[4, 5, 6, 7, 0, 1, 2]
🚨 Why Normal Binary Search Doesn’t Work Directly

Binary Search requires the entire array to be sorted.

In a rotated sorted array:

The full array is not sorted.

However, at least one half is always sorted.

👉 That is the key observation.

🔥 Core Intuition

At every step:

Calculate mid

Identify which half is sorted

Check if the target lies inside that sorted half

Discard the other half

Repeat until the element is found or the search space becomes empty.

📌 Key Observation

For any low, mid, and high:

If:

nums[low] <= nums[mid]

➡ The left half is sorted

Else:

➡ The right half is sorted

🎯 Decision Logic
Case 1: Left Half is Sorted

Check:

nums[low] <= target < nums[mid]

If TRUE → Search left

Else → Search right

Case 2: Right Half is Sorted

Check:

nums[mid] < target <= nums[high]

If TRUE → Search right

Else → Search left

✅ Implementation
def search_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[low] <= nums[mid]:
            
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Right half is sorted
        else:
            
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1
⏱ Complexity Analysis

Time Complexity: O(log n)

Space Complexity: O(1)

🧪 Practice Examples
Example 1
nums = [6,7,8,1,2,3,4,5]
target = 3

Try to dry run:

What is the first mid?

Which half is sorted?

What index should be returned?

Example 2
nums = [30,40,50,10,20]
target = 10

Questions:

Which half is sorted first?

Why?

Example 3 (Edge Case)
nums = [5,1,3]
target = 5