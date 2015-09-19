class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        self.result = []
        self.recurse(k, n, [], 0)
        return self.result
        
    def recurse(self, k, n, current, last):
        if last>9:
            return
        if k==0:
            if n==0:
                self.result.append(current)
        else:
            if n!=0:
                for num in range(last+1, 10):
                    if num>n:break
                    self.recurse(k-1, n-num, current+[num], num)

