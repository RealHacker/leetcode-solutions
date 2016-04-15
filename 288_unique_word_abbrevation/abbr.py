from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abr = defaultdict(set)
        for word in dictionary:
            shortened = self.shorten(word)
            self.abr[shortened].add(word)
    
    def shorten(self, word):
        if len(word)<=2:
            shortened = word
        else:
            shortened = word[0]+str(len(word)-2)+word[-1]
        return shortened
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        s = self.abr[self.shorten(word)]
        if word not in s and len(s)>=1:
            return False
        if word in s and len(s)>1:
            return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
