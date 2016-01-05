import operator
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maskLen = {self.getMask(word):len(word) for word in sorted(words, key=lambda w:len(w))}
        maxP = 0
        masks = sorted(maskLen.items(), key=operator.itemgetter(1))
        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                if masks[i][0]&masks[j][0]==0:
                    p = masks[i][1]*masks[j][1]
                    if p>maxP:
                        maxP = p
        return maxP
        
    def getMask(self, word):
        mask = 0
        for c in word:
            mask = mask|(1<<(ord(c)-97))
        return mask
