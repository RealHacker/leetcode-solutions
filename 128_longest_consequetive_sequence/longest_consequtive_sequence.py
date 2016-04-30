from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        _max = 1
        # build bi-directional graph
        for num in nums:
            if num in d: continue
            d[num] = []
            if num-1 in d:
                d[num].append(num-1)
                d[num-1].append(num)
            if num+1 in d:
                d[num+1].append(num)
                d[num].append(num+1)
                
        # find all connected components
        for num in nums:
            if num in d:
                q = [num]
                s = set()
                while q:
                    item = q.pop(0)
                    s.add(item)
                    for c in d[item]:
                        if c not in s:
                            q.append(c)
                    del d[item]
                if len(s)>_max:
                    _max = len(s)
                
        return _max
                
                
                
