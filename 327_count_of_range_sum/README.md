We can to record the sums, put sum from start up to index i into sums[i+1]. Then a O(N^2) solution is to loop over each pair of indices (i, j), if lower<=sums[j]-sums[i]<=upper, then we find a range with sum that satisfies the condition.

To do better, we have to divide and conquer. Observe that if we divide a range (I,J) into (I, mid) and (mid, J), then the pair of indices that satisfies the constraint have to be:

1. both between I and mid
2. both between mid and J
3. i is between I and mid, j is between mid and J

if we already solved the sub-problems of 1) and 2), we only need to count the pairs for 3).

If i is in (I, mid) and j is in (mid, J), then the order of 2 subsequences doesn't matter. We can sort both subsequences, and for each item i in range 1), use 2 cursors in range 2) to find the number of items j, with sums[j]-sum[i] between (lower, upper). Since the subsequence is ordered, the cursors can be reused in the inner loop for the next i.

The time complexity for this solution is O(N*log(N)).