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
        
        # the alphabet only includes the chars that appear in words        
        alphabet = set()
        for word in words:
            for c in word:
                alphabet.add(c)
        
        # toplogical sort
        degree_in = {}
        for char in alphabet:
            j = ord(char)-ord('a')
            degree_in[char]=sum([self.matrix[i][j] for i in range(26)])
        
        result = ""
        while True:
            hasZeroDegree=False
            for c in degree_in:
                if degree_in[c]==0:
                    hasZeroDegree = True
                    degree_in[c]=-1 # skip in the following checks
                    result += c
                    for k in range(26):
                        if self.matrix[ord(c)-ord('a')][k]>0:
                            degree_in[chr(ord('a')+k)]-=1
                    # print c
                    # print degree_in
            if not hasZeroDegree:
                if len(result)==len(alphabet):
                    return result
                return ""
            
    def add_to_mat(self, c1, c2):
        i1 = ord(c1)-ord('a')
        i2 = ord(c2)-ord('a')
        self.matrix[i1][i2]=1
        
