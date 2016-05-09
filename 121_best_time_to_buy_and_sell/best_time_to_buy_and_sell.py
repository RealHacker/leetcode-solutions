class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = high = current = prices[0]
        profit = 0
        for price in prices[1:]:
            if price >= current:
                high = price
            else:
                if high-low>profit:
                    profit = high - low
                if price<low:
                    low = price
                high = -1
            current = price
        if high-low>profit:
            profit = high-low
        return profit
