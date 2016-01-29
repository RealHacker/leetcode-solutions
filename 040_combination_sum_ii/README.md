A straightforward application of DP.

But you have to be clear how to divide the subproblems. 
My approach is:

1. sort the numbers in descending order
2. build a mapping from each unique number to its count

For a target number, compare it to nums[i]:

1. If nums[i]>target, you can not use it in the solution, reduce to subproblem for i+1;
2. If nums[i]<=target, nums[i] could appear 0-N times, where N is the largest number where N*nums[i]<=target.
For each of 0-N, solve the subproblem of i+1, and add nums[i] to the solutions. 