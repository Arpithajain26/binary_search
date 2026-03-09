### Intuition

The array is a **rotated sorted array that may contain duplicates**.
Because of the rotation, the array is not fully sorted, so we cannot directly apply normal binary search logic.

However, **at least one half of the array will always be sorted**. The idea is to identify the sorted half and check whether the target lies inside it.

1. **Binary Search Setup**

   * Use two pointers `low` and `high`.
   * Calculate `mid = (low + high) // 2`.

2. **Target Found**

   * If `nums[mid] == target`, return `True`.

3. **Handling Duplicates**

   * If `nums[low] == nums[mid] == nums[high]`, we cannot determine which half is sorted.
   * So we shrink the search space by doing:

     ```
     low += 1
     high -= 1
     ```

4. **Check Which Half is Sorted**

   **Case 1: Left Half is Sorted**

   ```
   nums[low] <= nums[mid]
   ```

   * If the target lies between `nums[low]` and `nums[mid]`, search in the **left half**.
   * Otherwise search in the **right half**.

   **Case 2: Right Half is Sorted**

   * If the target lies between `nums[mid]` and `nums[high]`, search in the **right half**.
   * Otherwise search in the **left half**.

5. **Repeat**

   * Continue narrowing the search range until the target is found or the search space becomes empty.

### Time Complexity

* Average case: **O(log n)**
* Worst case (due to duplicates): **O(n)**

### Space Complexity

* **O(1)** (no extra space used)
