This is a little non-obvious, but the problem can be solved in O(n) time. Just move forward the head cursor, and "shrink the tail" when duplicate chars appear, while maintaining the max substring length.

Need to take care of some special cases, like the start and end of string.

