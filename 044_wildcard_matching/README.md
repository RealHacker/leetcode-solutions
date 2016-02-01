It is easy to come up with the recursive backtracking solution (for each * in the pattern, the wildcard can match many char sequences). But the time complexity is exponential.


Here is my observation: 

1. If p starts with something other than *, s has to start with a matching substr.
2. If p ends with something other than *, s has to end with a matching substr.
3. If p starts and ends with *, I can split p by * into subpatterns, these subpatterns have to match sequentially in s.

So the algorithm is to consume the head and tail of p first, until p starts and ends with * (or p is empty). Then split p into subpatterns, find each subpattern sequentially in s, if all of them can be found, return True, else, return False. 