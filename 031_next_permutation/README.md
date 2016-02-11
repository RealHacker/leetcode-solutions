The key to this problem is this fact:

If the next greater permutation of X starts to differ from X from position i (common prefix from 0-i), then X[i+1:end] must be the greatest permutation for those elements. This means the elements i+1 to end must be in descending order. So to search for i, start from the end and search backwards for the first i where X[i]<X[i+1].

1. If i is negative, this means all elements are in descending order, and X is the greatest perm, return X reversed (smallest).
2. Else, search for the smallest element in i+1 to end that is larger than X[i], swap X[i] with it. And sort X[i+1:end] in ascending order.
