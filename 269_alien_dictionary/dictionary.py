class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.matrix = []
        for i in range(26):
            row = []
            for j in range(26):
                row.append(0)
            self.matrix.append(row)
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    self.add_to_mat(word1[j], word2[j])
                    break
                
        alphabet = set()
        for word in words:
            alphabet.add([c for c in word])
        
        # toplogical sort
        
    
    def add_to_mat(self, c1, c2):
        i1 = ord(c1)-ord('a')
        i2 = ord(c2)-ord('a')
        self.matrix[i1][i2]=1
        
