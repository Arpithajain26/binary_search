# 📘 Floor Element in a Sorted Array (Binary Search)

## 🔎 Problem Statement

Given a **sorted array** `nums` and a value `target`, find the **floor** of the target.

### 📌 Definition
The **floor** of a target is the **greatest element in the array that is less than or equal to the target**.

If no such element exists, return `-1`.

---

## 🧠 Intuition

Since the array is **sorted**, we can use **Binary Search** instead of linear search.

### 🔥 Key Idea

At any index `mid`:

- If `nums[mid] <= target`
  - This value can be a possible floor
  - But there might be a larger valid value on the right
  - So, store it and move right (`low = mid + 1`)

- If `nums[mid] > target`
  - This value cannot be the floor
  - So, move left (`high = mid - 1`)

We keep