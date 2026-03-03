# 📘 First and Last Occurrence in a Sorted Array (Binary Search)

## 🔎 Problem Statement

Given a **sorted array** `nums` and a value `target`,  
find the **first and last position** of the target.

If the target is not present, return `[-1, -1]`.

---

## 📌 Example

Input:
nums = [2, 4, 6, 8, 8, 8, 11, 13]
target = 8

Output:
[3, 5]

---

## 🧠 Intuition

Since the array is sorted, we can use **Binary Search**.

Instead of stopping when we find the target,  
we continue searching:

- 🔹 For **First Occurrence** → move LEFT after finding target  
- 🔹 For **Last Occurrence** → move RIGHT after finding target  

---

## 🎯 Key Logic

### 1️⃣ Finding First Occurrence

- If `nums[mid] == target`
  - Store index
  - Move left (`high = mid - 1`) to check if earlier occurrence exists

- If `nums[mid] < target`
  - Move right

- If `nums[mid] > target`
  - Move left

---

### 2️⃣ Finding Last Occurrence

- If `nums[mid] == target`
  - Store index
  - Move right (`low = mid + 1`) to check if later occurrence exists

- If `nums[mid] < target`
  - Move right

- If `nums[mid] > target`
  - Move left

---

## 💻 Implementation

```python
def first_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            high = mid - 1  # move left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def last_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            ans = mid
            low = mid + 1   # move right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


def first_and_last(nums, target):
    return [first_occurrence(nums, target),
            last_occurrence(nums, target)]


print(first_and_last([2,4,6,8,8,8,11,13], 8))