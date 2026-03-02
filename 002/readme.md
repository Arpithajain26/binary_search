# Upper Bound using Binary Search

## 📌 Problem Description
Given a **sorted array** and a **target value**, find the **index of the first element that is strictly greater than the target**.

This concept is known as **Upper Bound**.

---

## 💡 Intuition

Since the array is sorted, we can use **Binary Search** to efficiently find the upper bound.

👉 The key idea is:
> Do not stop when you find the target.  
> Keep searching towards the **left** to find the **first element greater than the target**.

---

## 🧠 Step-by-Step Thinking

1. **Search Space**
   - Start with the entire array
   - `low = 0`, `high = n - 1`

2. **Answer Initialization**
   - Initialize `ans = len(arr)`
   - This acts as a **default value** if no element greater than the target exists

3. **Binary Search Logic**
   - Calculate the middle index:
     ```
     mid = (low + high) // 2
     ```

4. **Comparison**
   - If `arr[mid] > target`:
     - This index could be the upper bound
     - Store it in `ans`
     - Move left to find a smaller valid index
   - Else:
     - Move right

5. **Termination**
   - When `low > high`, the loop ends
   - `ans` contains the **upper bound index**

---

## 🧪 Example Walkthrough

**Input:**Array = [1, 2, 3, 4, 5, 6,7, 8]
Target = 5

| Step | low | high | mid | arr[mid] | Action |
|-----|-----|------|-----|----------|--------|
| 1 | 0 | 7 | 3 | 4 | Move right |
| 2 | 4 | 7 | 5 | 6 | ans = 5, move left |
| 3 | 4 | 4 | 4 | 5 | Move right |

✅ **Upper Bound Index = 5**

---

## 🧾 Code Implementation

```python
def upper_bound(arr, target):
    ans = len(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

print(upper_bound([1,2,3,4,5,6,7,8], 5))
