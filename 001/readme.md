📌 Intuition Behind the Algorithm (Lower Bound using Binary Search)
Problem Idea

Given a sorted array, we want to find the first index where the element is greater than or equal to a given target value.

This concept is commonly known as Lower Bound.

Why Binary Search?

The array is sorted

Linear search takes O(n) time

Binary search reduces it to O(log n) by repeatedly halving the search space

Core Intuition

Instead of stopping when we find the target:

We continue searching on the left side

This ensures we find the first valid position

Step-by-Step Thinking

Search Space

Start with the full array

low = 0, high = n - 1

Possible Answer

Initialize ans = n

This acts as a default if no element ≥ target exists

Mid Calculation

Compute middle index:

mid = (low + high) // 2

Comparison Logic

If arr[mid] >= target:

This index could be an answer

Store it in ans

Move left to find a smaller valid index

Else:

Element is too small

Move right

Termination

Loop ends when low > high

ans contains the lower bound index

Example Walkthrough
Array  = [1, 2, 3, 4, 5, 6, 7, 8]
Target = 5
Step	low	high	mid	arr[mid]	Action
1	0	7	3	4	Move right
2	4	7	5	6	Store ans=5, move left
3	4	4	4	5	Store ans=4, move left

✅ Final Answer: Index 4