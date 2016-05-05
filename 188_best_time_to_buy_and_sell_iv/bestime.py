class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        buy = [] # buy[i][k] stands for: for first i prices, maximum profit if transacted k time and last is buy
        sell = []
        
        if k>len(prices)/2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i]>prices[i-1]:
                    profit+= prices[i]-prices[i-1]
            return profit
            
        for i,price in enumerate(prices):
            if not buy:
                brow = [0] + [-price]*k
                srow = [0]*(k+1)
            else:
                brow = [0]
                srow = [0]
                for j in range(1, k+1):
                    maxb = max(buy[i-1][j], sell[i-1][j-1]-price)
                    brow.append(maxb)
                    maxs = max(sell[i-1][j], buy[i-1][j]+price)a
                    srow.append(maxs)
            buy.append(brow)
            sell.append(srow)
        
        return sell[-1][k]
                
