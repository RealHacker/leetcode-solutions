class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.trie = {}
        self.buildtrie(words)
        results = []
        for j, word in enumerate(words):
            node = self.trie
            for i in range(len(word)):
                if 'idx' in node:
                    if node['idx']!=j:
                        rest = word[i:]
                        if rest=="".join(reversed(rest)):
                            results.append([j, node['idx']])
                c = word[i]
                if c in node:
                    node = node[c]
                else:
                    break
            else:
                if 'pal' not in node:
                    result = []
                    result = self.getpal(node, "")
                    node['pal'] = result
                    
                for v in node['pal']:
                    if v!=j:
                        results.append([j, v])
        return results
        
    def getpal(self, node, s):
        result = []
        for k in node:
            if k=='idx':
                if s=="".join(reversed(s)):
                    # print "here"
                    result.append(node['idx'])
            elif k!='pal':
                r = self.getpal(node[k], s+k)
                result += r
        return result
    
    def buildtrie(self, words):
        for i,word in enumerate(words):
            r = reversed(word)
            node = self.trie
            for c in r:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['idx'] = i

        
