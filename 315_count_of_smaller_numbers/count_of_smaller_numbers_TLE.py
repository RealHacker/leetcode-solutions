class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs = [(i, num) for i, num in enumerate(nums)]
        s = []
        d = {}
        for pair in pairs:
            if not s:
                s.append(pair)
                d[pair[0]] = 0
            else:
                i =0
                while i<len(s):
                    if pair[1]>=s[i][1]:
                        i+=1
                    else:
                        break
                s.insert(i, pair)
                d[pair[0]] = i
        print s
        newpairs = [(j-d[pair[0]], pair[0]) for j,pair in enumerate(s)]
        newpairs = sorted(newpairs, key = operator.itemgetter(1))
        return [p[0] for p in newpairs]
        
