First, the most obvious solution is to just keep the numbers, and compute the range sum by iterating over the elements in the range. The update is O(1), rangeSum is O(N).

The next idea is to maintain a list of partial sums array,
sums[i] is the sum of all elements up to index i. Now, when updating a element i, every sum element after i needs to be updated with the diff, a O(N) operation. rangeSum is sum[j]-sum[i], a O(1) operation.

It all depends on how these 2 operations are distributed. If both operations are very frequent, then a Log(N) algorithm is required. 

This is where BIT (binary index tree) comes in. The best material I find about BIT is here:
[
http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a](http://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a)