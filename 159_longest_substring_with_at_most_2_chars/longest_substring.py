class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        c = s[0]
        maxlen = 0
        chars = set([c])
        llen = 0
        start = 0
        end = 0
        for i,cc in enumerate(s):
            if cc==c:
                end +=1
                llen +=1
            elif cc in chars:
                c = cc
                start = i-1
                end = i
                llen += 1
            elif len(chars)==1:
                c = cc
                chars.add(cc)
                start = i-1
                end = i
                llen += 1
            else:
                if llen>maxlen: maxlen = llen
                chars = set([c, cc])
                c = cc
                llen = end-start+1
                start = i-1
                end = i
            #print cc, c, start, end, llen, chars
        if llen>maxlen: maxlen = llen
        
        return maxlen
                
                
                
