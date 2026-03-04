# Count Occurrences of Target in an Array

## 📌 Problem Statement

Given a list of integers `nums` and an integer `target`, return the number of times `target` appears in the list.

---

## 🧠 Intuition

To count how many times a number appears in a list, we must check each element one by one.

The approach is simple:

1. Initialize a counter variable `count = 0`
2. Traverse through the list
3. If the current element equals `target`, increment `count`
4. Return `count` at the end

This method is called **linear traversal**.

---

## 🔎 Example

### Input

```python
nums = [1, 2, 2, 2, 3, 4, 4]
target = 2