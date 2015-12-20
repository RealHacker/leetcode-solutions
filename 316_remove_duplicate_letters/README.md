This problem can be solved with either a greedy method or by backtracking.

## Greedy ##
Get the sorted alphabet for the characters in the string, pick the the smallest char, whose leftmost index idx satisfies:

	set(s[idx:]) == set(s)

Thus, we guarantees all the characters in s still has a chance to be picked.

## Backtracking ##
Maintain the last index for each character in s in a map rindex. And when looping over the string, before putting the char in result, check the end of current result backwards,
	 
	if result[-1]>c and rindex[result[-1]]>current_position:
		result = result[:-1]

By repeatedly adjusting the tail of result string, we maintain the minimum result property.