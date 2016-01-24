class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs = [(num, i) for i, num in enumerate(nums)]
        s = []
        d = {}
        for pair in pairs:
            i =bisect.bisect_right(s, pair)
            s.insert(i, pair)
            d[pair[1]] = i
        #print s
        newpairs = [(j-d[pair[1]], pair[1]) for j,pair in enumerate(s)]
        newpairs = sorted(newpairs, key = operator.itemgetter(1))
        return [p[0] for p in newpairs]
        
