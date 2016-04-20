class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.memo = {}
        ret =self.recurse(word)
        return ret
        
    def recurse(self, word):
        if not word:return [""]
        if word in self.memo:
            return self.memo[word]
        results = [word]
        for i in range(len(word)):
            digits = str(i+1)
            for j in range(len(word)-i):
                suffixes = self.recurse(word[i+j+2:])
                for suffix in suffixes:
                    if i+j+1<len(word):
                        results.append(word[:j]+digits+word[i+j+1]+suffix)
                    else:
                        results.append(word[:j]+digits)
        self.memo[word] = results
        return results
                
