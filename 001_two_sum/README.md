The naive solution of iterating over nums in 2 passes is O(N^2).

We can solve this by first sorting the nums, and use the classic algorithm of 2 cursors moving from the start and end, towards each other. Time complexity is O(NlogN).

