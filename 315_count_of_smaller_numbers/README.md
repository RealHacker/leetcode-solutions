This problem can be solved by sorting:

We will do insertion sort with binary search to find the place to insert, we need to record 2 things for each number:

1. C1 - The number of elements less than or equal to N when N is inserted
2. C2 - The index of N after the whole list has been sorted

`C2-C1` is the number of smaller element after N

But we need to output the counts in original sequence, this can be done by carrying the original index with the number, and finally sorting by this index. 