On first thought, this appears to be a O(N^2) problem.

But actually, it can be solved in a single pass: maintain a partial sum, when it is positive, add it to element i, else, reset sum from element i (sum = nums[i]).

Time: O(N).