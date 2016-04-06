class Solution(object):
    pairs = [("0","0"), ("1","1"),("8","8"),("6","9"), ("9","6")]
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.recurse(n, n)
        
    def recurse(self, n, N):
        if n==0:
            return [""]
        elif n==1:
            return ["0", "1", "8"]
        else:
            result = []
            if n!=N:
                for s in self.recurse(n-2, N):
                    for prefix, suffix in self.pairs:
                        result.append(prefix+s+suffix)
            else:
                for s in self.recurse(n-2, N):
                    for prefix, suffix in self.pairs[1:]:
                        result.append(prefix+s+suffix)
            return result
