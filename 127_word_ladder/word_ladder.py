import string
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
        wordList.add(endWord)

        q = [(beginWord,1)]
        visited = set()
        visited.add(beginWord)
        while True:
            if not q: break
            w, c = q.pop(0)
            if w==endWord: 
                return c
            for i in range(0, len(w)):
                for ch in string.lowercase:
                    if ch == w[i]: continue
                    word = w[:i]+ch+w[i+1:]
                    if word in wordList and word not in visited:
                        if word == endWord: return c+1
                        visited.add(word)
                        q.append((word, c+1))
        return 0
