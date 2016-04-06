class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = -1
        idx2 = -1
        shortest = len(words)+1
        for i, word in enumerate(words):
            if word==word1:
                idx1 = i
                if idx2>=0 and idx1-idx2<shortest:
                    shortest = idx1-idx2
            elif word==word2:
                idx2 = i 
                if idx1>=0 and idx2-idx1<shortest:
                    shortest = idx2-idx1
        return shortest
                    
