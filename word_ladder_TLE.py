class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def diff(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    diff += 1
                if diff >1:
                    break
            return diff==1
            
        graph = {}
        for word in wordList:
            d = []
            for w in wordList:
                if word==w:break
                if diff(word, w):
                    d.append(w)
            graph[word] = d
        print "graph"
        
        q = [(beginWord,0)]
        visited = set()
        visited.add(beginWord)
        while True:
            if not q: break
            w, c = q.pop(0)
            if w==endWord: 
                return c
            for word in graph[w]:
                if word not in visited:
                    if word == endWord: return c+1
                    visited.add(word)
                    q.append((word, c+1))

        return 0
        
        