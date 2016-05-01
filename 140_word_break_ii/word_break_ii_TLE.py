class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not wordDict:
            return False
        self.memo = {}
        self.maxlength = max([len(word) for word in wordDict]) 
        return self.recurse(s, wordDict)
        
    def recurse(self, s, wordDict):
        if not s:
            return [""]
        if s in self.memo:
            return self.memo[s]
        results = []
        for i in range(1, self.maxlength):
            if s[:i] in wordDict:
                sub = self.recurse(s[i:], wordDict)
                results += [s[:i]+" "+substr for substr in sub]
        self.memo = results
        return self.memo
        
                
                
