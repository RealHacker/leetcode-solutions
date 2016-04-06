from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.indice = defaultdict(list)
        self.memo = {}
        self.MAXLEN = len(words)
        for i, word in enumerate(words):
            self.indice[word].append(i)
        
    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]
            
        l1, l2 = self.indice[word1], self.indice[word2]

        idx1, idx2 = 0, 0
        min_distance = self.MAXLEN
        while True:
            if idx1 >= len(l1) or idx2 >= len(l2):
                break
            if l1[idx1]<l2[idx2]:
                if l2[idx2]-l1[idx1]<min_distance:
                    min_distance = l2[idx2]-l1[idx1]
                idx1 +=1
            else:
                if l1[idx1]-l2[idx2]<min_distance:
                    min_distance = l1[idx1]-l2[idx2]
                idx2+=1
        self.memo[(word1, word2)] = min_distance
        return min_distance
            
            
# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
