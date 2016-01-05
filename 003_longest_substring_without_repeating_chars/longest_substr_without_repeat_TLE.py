class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # mark the positions of each individual char
        pos = {}
        duplicates = set()
        for i, c in enumerate(s):
            pos.setdefault(c, []).append(i)
            if len(pos[c])>=2:
                duplicates.add(c)
            
        pairs = []
        for i, c in enumerate(s):
            if c in duplicates:
                pairs.append((i, c))
        if not pairs:
            return len(s)
        _start, _end = object(), object()
        if pairs[0][0]>0:
            pairs.insert(0, (0, _start))
        if pairs[1][0]<len(s)-1:
            pairs.append((len(s)-1, _end))

        lmax = 0 
        for i, pair in enumerate(pairs):
            mm, cc = pair
            seen = set([cc])
            idx = i+1
            while idx<len(pairs):
                k, c = pairs[idx]
                if c in seen:
                    if k-mm>lmax:
                        lmax = k-mm
                    break
                seen.add(c)
                idx += 1
            if idx == len(pairs):
                lmax = max(lmax, len(s)-mm)
                
        return lmax





        # cadidate intervals that can be longest nonrepeating substr
        # intervals = {}
        # for c in pos:
        #     vec = pos[c]
        #     vec.insert(0, -1)
        #     vec.append(len(s))
        #     ints = []
        #     i = 0
        #     while i+2<len(vec):
        #         ints.append((vec[i]+1, vec[i+2]-1))
        #         i+=1
        #     intervals[c]=ints
        # print intervals
        
        # maxlen = 0   
        # for c in intervals:
        #     for interval in intervals[c]:
        #         substr = s[interval[0]:interval[1]+1]
        #         setlen = len(set(substr))
        #         strlen = len(substr)
        #         if setlen == strlen and strlen > maxlen:
        #             maxlen = strlen
        # return maxlen


print Solution().lengthOfLongestSubstring("c")
