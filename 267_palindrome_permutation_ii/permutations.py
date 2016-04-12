from collections import defaultdict
from itertools import permutations
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        oddchar = None
        odd = 0
        pairs = []
        for c in d:
            if d[c]%2!=0:
                oddchar = c
                odd += 1
            pairs += [c] * (d[c]/2)
        if odd>1:
            return []
        candidates = set(list(permutations(pairs)))
        results = []
        for candidate in candidates:
            if oddchar:
                results.append(''.join(candidate)+oddchar+''.join(candidate[::-1]))
            else:
                results.append(''.join(candidate)+''.join(candidate[::-1]))
        return results
            
