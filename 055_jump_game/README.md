To reach the end of the jump game, 2 conditions have to be satisfied:

1. for some i, i+a[i]>=len(a)-1
2. This i has to be reachable, meaning for some j: j+a[j]>=i

So the algorithm loops over the array, maintaining the furthest index reachable.
If current index>reachable, return False, because the end is not reachable.
Otherwise, when reachable >= end, return True. 