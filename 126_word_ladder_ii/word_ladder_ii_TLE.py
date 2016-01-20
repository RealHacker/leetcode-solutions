import string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
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
        
        shortest = -1
        solutions = []
        q = [[beginWord]]

        while True:
            if not q: break
            ws = q.pop(0)
            print q
            if shortest>0 and len(ws)>=shortest:
                break
            if ws[-1]==endWord: 
                solutions.append(ws)
            w = ws[-1]
            for i in range(0, len(w)):
                for ch in string.lowercase:
                    if ch == w[i]: continue
                    word = w[:i]+ch+w[i+1:]
                    if word in wordList and word not in ws:
                        if word == endWord: 
                            news = ws+[word]
                            solutions.append(news)
                            if shortest<0:
                                shortest = len(news)

                        q.append(ws+[word])
        return solutions