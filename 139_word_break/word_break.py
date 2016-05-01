class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        self.tree = {}
        self.memo = {}
        for word in wordDict:
            self.buildNode(word, self.tree)
        return self.traverse(s)
            
    def traverse(self, s):
            if s in self.memo:
                return self.memo[s]
            if not s:
                return True
            ret = False
            root = self.tree
            for i in range(len(s)+1):
                if -1 in root:
                    if self.traverse(s[i:]):
                        ret = True
                        break
                if i < len(s):
                    c = s[i]
                    if c in root:
                        root = root[c]
                    else:
                        break
            
            self.memo[s] = ret
            return ret
                    
    def buildNode(self, word, tree):
        if not word:
            tree[-1] = True
        else:
            c = word[0]
            if c not in tree:
                tree[c] = {}
            self.buildNode(word[1:], tree[c])
