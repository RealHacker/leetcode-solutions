class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.wins = set()
        return self.recurse(s)
    
    def recurse(self, s):
        if s in self.wins:
            return True

        canWin = False
        for i in range(len(s)-1):
            if s[i:i+2]=="++":
                news = s[:i]+"--"+s[i+2:]
                if not self.recurse(news):
                    canWin = True
                    break
        if canWin:
            self.wins.add(s)
        return canWin
