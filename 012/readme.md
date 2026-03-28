In a sorted array where every element appears exactly twice except one, the key observation lies in how pairs are arranged.

🔍 Pairing Pattern

Before the single element
Elements form perfect pairs:

[1,1, 2,2, 3,3]
 ↑    ↑    ↑
even indices match with next element

After the single element
The pattern shifts:

[4, 5,5, 6,6]
 ↑
single element breaks the pairing pattern
💡 Core Idea
In the left half, pairs follow a consistent rule:
Even index → matches next element
Odd index → matches previous element
Once we cross the single element, this pattern breaks.
🚀 How Each Approach Uses This
1. Brute Force
Simply checks each element’s neighbors
If an element is not equal to both left and right → it is the answer
2. Binary Search (Optimized)
Instead of scanning all elements, we:
Check if the current index follows the pairing pattern
If pattern is correct → move right
If pattern is broken → move left

👉 This allows us to eliminate half of the array each time

🎯 Key Insight

As long as the pairing pattern is correct, the single element lies ahead.
Once the pattern breaks, the single element lies behind.

📌 Why This Works
The array is sorted, so duplicates are adjacent
The single element shifts the pairing structure
Binary search detects this shift efficiently