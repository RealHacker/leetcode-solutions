class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        return self.recurse(0, 1, 0)
        
    def recurse(self, idx, state, price):
        if idx >= len(self.prices): 
            return 0
        # 2 kinds of state: [bought - 0, sold - 1]
        if state==0:
            if self.prices[idx]>price:
                p1 = (self.prices[idx]-price)+self.recurse(idx+2, 1, 0)
                p2 = self.recurse(idx+1, 0, price)
                return max(p1, p2)
            else:
                return self.recurse(idx+1, 0, price)
        else:
            p1 = self.recurse(idx, 0, self.prices[idx])
            p2 = self.recurse(idx+1, 1, 0)
            return max(p1, p2)
            
