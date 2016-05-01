class Solution(object):
    def wordBreak(self, s, wordDict):
        self.tree = {}
        self.memo = {}
        for word in wordDict:
            self.buildNode(word, self.tree)
        self.splits = {}
        
        self.traverse(s, 0)
        
        return self.gen(s, len(s))
    
    def buildNode(self, word, tree):
        if not word:
            tree[-1] = True
        else:
            c = word[0]
            if c not in tree:
                tree[c] = {}
            self.buildNode(word[1:], tree[c])
    
    def gen(self, s, n):
        if n==0:
            return [""]
        results = []
        if not self.splits or n not in self.splits:
            return []
        for x in self.splits[n]:
            for ss in self.gen(s, x):
                if ss:
                    results.append(ss+" "+s[x:n])
                else:
                    results.append(s[x:n])
        return results
            
    def traverse(self, s, idx):
        if idx == len(s):
            return
        i = idx
        node = self.tree
        while True:
            if -1 in node:
                if i not in self.splits:
                    self.splits[i]=[idx]
                    self.traverse(s, i)
                elif idx not in self.splits[i]:
                    self.splits[i].append(idx)
                    
            if i >= len(s):
                return
            else:
                c = s[i]
                if c in node:
                    node = node[c]
                    i = i+1
                else:
                    return
        
                
                
            
        
           
                    
    
