class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        
        buy = [-prices[0]]
        sell = [0]
        
        for i in range(1, len(prices)):
            newbuy = max(buy[i-1], (sell[i-2] if i>=2 else 0) - prices[i])
            newsell = max(sell[i-1], buy[i-1]+prices[i])
            buy.append(newbuy)
            sell.append(newsell)
        
        return sell[-1]
        
    
