Finding the Smallest Element in a Rotated Sorted Array
Problem Intuition

A rotated sorted array is an array that was originally sorted in ascending order but then rotated at some pivot point.

Example:

Original sorted array

[0, 1, 2, 4, 5, 6]

After rotation

[4, 5, 6, 0, 1, 2]

The smallest element becomes the pivot point where the rotation happened.

Our goal is to find the smallest element efficiently.

Key Idea (Binary Search Insight)

Since the array was originally sorted, we can use Binary Search instead of scanning the whole array.

Binary search works because at least one half of the array will always be sorted.

We check which side is sorted and eliminate the other half.

Observations
Case 1: Entire Search Space is Sorted

If

nums[low] <= nums[high]

then the entire portion is already sorted.

Therefore the smallest element is simply nums[low].

Example

[0,1,2,4,5]

We stop immediately.

Case 2: Left Half is Sorted

If

nums[low] <= nums[mid]

Example

[4,5,6 | 0,1,2]
 low   mid

The left half [4,5,6] is sorted.

So the smallest element cannot be inside this sorted portion except at low.

We store

ans = min(ans, nums[low])

and search the right half.

low = mid + 1
Case 3: Right Half is Sorted

Otherwise the rotation point lies in the left half.

Example

[4,5,6,0 | 1,2]
        mid

The smallest element could be at mid.

So we update

ans = min(ans, nums[mid])

and move to the left side.

high = mid - 1
Algorithm Steps

Initialize two pointers

low = 0
high = n-1

Maintain a variable to store the smallest value

ans = infinity

While low <= high

Check if current portion is sorted

Identify which half is sorted

Discard the sorted half

Continue searching in the unsorted half

Return ans

Time Complexity
O(log n)

Because we eliminate half of the array every iteration.

Space Complexity
O(1)

No extra memory is used.

Example Walkthrough

Array

[4,5,6,0,1,2]

Step 1

low = 0
high = 5
mid = 2

Left half [4,5,6] is sorted.

ans = 4
low = mid + 1

Step 2

low = 3
high = 5

Array is sorted

[0,1,2]

So

ans = min(4,0) = 0

Final Answer

0