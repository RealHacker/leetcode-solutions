
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        self.coins = set(coins)
        min_coin = min(coins)
        d = [sys.maxint]*(amount+1)

        for i in range(min_coin, amount+1):
            if i in self.coins:
                d[i] = 1
            else:
                for coin in self.coins:
                    if i-coin>0 and d[i-coin]!=sys.maxint:
                        d[i] = min(d[i], d[i-coin]+1)
        if d[amount]==sys.maxint:
            return -1
        return d[amount]
