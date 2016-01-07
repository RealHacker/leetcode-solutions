This is obviously a DP problem.

But it is hard to partition it into sub-problems because of operator precedence:
	
	1+2*3+4

If we partition the problem into `12` and `34`, then the values calculated from subproblems cannot be used to construct solution 
for the big problem. So we need 2 levels of recursion:

First level is for `+` and `-`, second level is for `*` operator.

For each finished expression like `1*2+3-4`, we find the leftmost + or - operator, character to its left is either an atomic number 
or a `*` expression, then we can recurse with `*` on the left, and recurse with `+` or `-` on the right.

There is a minor problem with "-" operator:
	
	1-2+3 is not equal to 1-(2+3)

We can treat minus as adding a negative number. For every atomic number or `*` expression, we consider adding either the number or
its negative number, and adjust the expression accordingly.

In the end, we need to filter out expressions that starts with a "-" sign. (Because operators are only allowed *between* numbers).
