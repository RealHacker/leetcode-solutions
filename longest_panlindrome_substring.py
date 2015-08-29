class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        maxlen = 0
        for i in range(len(s)):
            start = i
            end = i
            while start>=0 and end<len(s):
                if s[start]!=s[end]:                    
                    break
                if end-start+1>maxlen:
                    maxlen = end-start+1
                    longest = s[start:end+1]                
                start-=1
                end+=1
            start = i
            end = i+1
            while start>=0 and end<len(s):
                if s[start]!=s[end]:                    
                    break
                if end-start+1>maxlen:
                    maxlen = end-start+1
                    longest = s[start:end+1]                
                start-=1
                end+=1
        return longest 

print Solution().longestPalindrome("VABBCBBAS")
