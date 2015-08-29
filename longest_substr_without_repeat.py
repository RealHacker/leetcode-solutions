class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # mark the positions of each individual char
        pos = {}
        for i, c in enumerate(s):
            pos.setdefault(c, []).append(i)
            
        # cadidate intervals that can be longest nonrepeating substr
        intervals = {}
        for c in pos:
            vec = pos[c]
            vec.insert(0, -1)
            vec.append(len(s))
            ints = []
            i = 0
            while i+2<len(vec):
                ints.append((vec[i]+1, vec[i+2]-1))
                i+=1
            intervals[c]=ints
        print intervals
        
        maxlen = 0   
        for c in intervals:
            for interval in intervals[c]:
                substr = s[interval[0]:interval[1]+1]
                setlen = len(set(substr))
                strlen = len(substr)
                if setlen == strlen and strlen > maxlen:
                    maxlen = strlen
        return maxlen


print Solution().lengthOfLongestSubstring("c")
