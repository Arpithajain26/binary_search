🔷 1. What is a Peak Element?

A peak element is an element which is greater than its neighbors.

👉 Condition:

nums[i] > nums[i-1] (left)
nums[i] > nums[i+1] (right)

Edge cases:

First element → only check right
Last element → only check left
🔷 2. First Function (Brute Force)
def peak_element(nums):
    for i in range(len(nums)):
        if (i==0 or nums[i-1]<nums[i]) and (i==len(nums)-1 or nums[i]>nums[i+1]):
            return nums[i]
🧠 Intuition

👉 You are checking every element:

“Am I greater than my left?”
“Am I greater than my right?”

If YES → return it.

📌 Example

[1,2,3,4,5,6,7,8,5,1]

At 8:

Left = 7 ✅
Right = 5 ✅

➡️ So 8 is peak.

⏱ Complexity
Time: O(n) (linear scan)
Space: O(1)
🔑 Key Idea

👉 “Check all elements one by one”

🔷 3. Second Function (Binary Search Optimization)
def peak_element1(nums):
🧠 Core Intuition (VERY IMPORTANT)

👉 Instead of checking all elements, we use the pattern of the array

💡 Observation:

If:

nums[mid] > nums[mid-1] → you are in increasing slope
→ peak lies on right side
nums[mid] > nums[mid+1] → you are in decreasing slope
→ peak lies on left side
🧭 Visual Understanding

Example:

1  2  3  4  5  6  7  8  5  1
                     ↑ peak
Case 1: Increasing slope
1 2 3 4 5
        ↑

➡️ Move RIGHT

Case 2: Decreasing slope
8 5 1
↑

➡️ Move LEFT

🔁 Binary Search Logic
mid = (low + high) // 2
Cases:
✅ Case 1: Found Peak
nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]
➡️ Case 2: Increasing slope
nums[mid] > nums[mid-1]

➡️ Move right:

low = mid + 1
⬅️ Case 3: Decreasing slope
nums[mid] > nums[mid+1]

➡️ Move left:

high = mid - 1
⚠️ Small Mistake in Your Code
if nums[n-1] > nums[n-2]:
    return n-1   # ❌ returning index

👉 Should be:

return nums[n-1]   # ✅ return value (to match first function)
⏱ Complexity
Time: O(log n) 🔥
Space: O(1)