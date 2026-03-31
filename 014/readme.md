Square Root (Floor Value) – Intuition Guide
🎯 Problem Statement

Given a number num, find the floor value of its square root.

👉 Example:
√28 ≈ 5.29 → Answer = 5

🧠 Approach 1: Brute Force
def squareroot(num):
    ans = 0
    for i in range(num):
        if (i * i <= num):
            ans = i
        else:
            break
    return ans
💡 Intuition (Very Important)
Start from i = 0

Keep checking:

i * i ≤ num
As long as condition is true → update answer
The moment it becomes false → stop
🔍 Example (num = 28)
i	i²	Condition	ans
1	1	≤ 28 ✅	1
2	4	≤ 28 ✅	2
3	9	≤ 28 ✅	3
4	16	≤ 28 ✅	4
5	25	≤ 28 ✅	5
6	36	> 28 ❌	stop

👉 Final Answer = 5

⏱️ Complexity
Time: O(n)
Not efficient for large numbers ❌
🚀 Approach 2: Binary Search (Optimized)
def squareroot1(num):
    low = 1
    high = num
    ans = 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid <= num:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
🧠 Core Intuition (MOST IMPORTANT 🔥)

We are searching for:

largest number whose square ≤ num
⚡ Binary Search Thinking

Instead of checking all numbers:
👉 We divide the search space

Range:

1 → num
🔄 Decision Logic
Case 1:
mid² ≤ num

✔ mid is a valid answer
👉 But maybe a bigger one exists

➡️ Move RIGHT:

low = mid + 1
Case 2:
mid² > num

❌ mid is too large

➡️ Move LEFT:

high = mid - 1
🔍 Example (num = 28)
low	high	mid	mid²	Action
1	28	14	196 ❌	left
1	13	7	49 ❌	left
1	6	3	9 ✅	right
4	6	5	25 ✅	right
6	6	6	36 ❌	left

👉 Final Answer = 5

⏱️ Complexity
Time: O(log n) ✅ (very efficient)
