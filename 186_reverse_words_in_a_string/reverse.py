class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if not s:
            return
        start=-1
        for i, c in enumerate(s):
            if c==" ":
                if start>=0:
                    for k in range((i-start)/2):
                      s[start+k], s[i-1-k] = s[i-1-k], s[start+k]
                    start = -1
            else:
                if start<0:
                    start = i
        i = len(s)
        if start>=0:
            for k in range((i-start)/2):
                s[start+k], s[i-1-k] = s[i-1-k], s[start+k]
        s.reverse()
        
