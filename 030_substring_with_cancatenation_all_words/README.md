This problem can be solved in O(NK).

Assuming the length of each word is K, then no matter how long the string is, a match can be found by starting at position (0 to K-1) and advance by units of K.

For each of the K starting positions, we can find all matches in a single pass by maintaining 2 cursors, one pointing at the start of current cancatenation, and the other at the end. And we take the next K chars and compare it to words:

1. If it is not in words, matching fails. We advance both start and end to current position + K.
2. If it is in words, and count of this word is less than or equal to the required word count, we update the counter, and advance the end cursor.
3. If it is in words, but count of this word exceeds the limit, we trim the start word - advance the start cursor, and update the counter by decrementing the count for start word.