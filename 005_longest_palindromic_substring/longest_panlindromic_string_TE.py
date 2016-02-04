from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
         # A char -> [list of indice]
        matrix = defaultdict(bool)
        result = ""
        # initialize 
        for i in range(len(s)):
            matrix[(i,i)] =True
        # N*N
        maxlen = 1
        result = ""
        for diff in range(1, len(s)):
            for x in range(len(s)-diff):
                if s[x]==s[x+diff] and (diff==1 or matrix[(x+1,x+diff-1)]):
                    matrix[(x,x+diff)]=True
                    if diff>maxlen:
                        maxlen = diff
                        result = s[x:x+diff+1]
            if maxlen<diff:
                break
        return result
                    
                    
                    
        
            
        