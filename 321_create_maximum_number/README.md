At first, this solution looks like this:

Find the largest digit starting from the beginning of num1 and num2, and append to the result, subject to one restriction - the number of digits left in num1 and num2 (after taking the digit) have to be greater than or equal to k-1.

My first solution: for the largest digit found, try every valid position of this digit in both num1 and num2, and recurse. TLE. Then I start to look for optimizations.

My second solution: for the largest digit, I only look at the first valid position in each num, that should be enough, and I eliminate the need of an inner loop by using a radix bucket for [0-9].

But the result is still TLE. The time complexity is still exponential in the worst case; O(2^k) - each time I pick the next digit, there are 2 possible choices.

Then it occurs to me that I can deal with num1 and num2 independantly: If I find the largest subsequence of length l1 for num1, and largest subsequence of length l2 for num2, I can get the largest sequence of length l1+l2 by merging the two. The result of this problem can be broken into LS of num1 and LS of num2, this can be proved by contradiction.

So in the end, the solution is:

	For i in range(0, len(num1)):
		find largest subsequence of length i from num1
		find largest subsequence of length (k-i) from num2
		merge the 2 by picking the larger value from the left side of 2 subsequences

There is one more detail, during the merge, if s[0]==s[1], then what? The intuition is "it doesn't matter, to pick either one is ok", but actually, it matters:

	355555
    366666

If I pick the first 3, the result is 355555366666, else, the result is 366666355555.

You have to compare the whole sequence to decide which num to pick.   