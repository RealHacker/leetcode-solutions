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
        d = {}
        start = 0
        lmax = 0
        cnt = 0
        for pos, c in pairs:
            if c not in d:
                d[c]=pos
            else:
                if pos-start>lmax:
                    lmax = pos-start
                start = max(start, d[c]+1)
                d[c] = pos
                #print pos, start, lmax
            cnt += 1
        if cnt == len(pairs):
            lmax = max(lmax, len(s)-start)

        return lmax


print Solution().lengthOfLongestSubstring("c")
