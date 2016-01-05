import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.d = {}
        self.coins = sorted(coins)
        if amount==0: return 0
        return self.recurse(amount)
    
    def recurse(self, n):
        if n in self.d:
            return self.d[n]
        elif n<self.coins[0]:
            result = -1
        elif n in self.coins:
            result = 1
        else:
            min = sys.maxint
            found = False
            for coin in self.coins:
                t = self.recurse(n-coin)
                if t > 0 and t+1<min:
                    min = t+1
                    found = True
            if not found:
                result = -1
            else:
                result = min
        self.d[n]=result
 
        return result
