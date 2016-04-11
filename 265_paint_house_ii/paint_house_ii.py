import sys
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        if not costs:
            return 0
        self.costs = costs
        self.memo = {}
        self.k = len(costs[0])
        mincost = sys.maxint
        for i in range(self.k):
            mincost = min(mincost, self.recurse(0, i))
        return mincost

    def recurse(self, start_index, color):
        if start_index==len(self.costs):
            return 0
        if (start_index, color) not in self.memo:
            cost = self.costs[start_index][color]
            _min = sys.maxint
            for c in range(self.k):
                if c!=color or start_index+1==len(self.costs):
                    _min = min(_min, self.recurse(start_index+1, c))
            self.memo[(start_index, color)] = cost+_min
        return self.memo[(start_index, color)]
        
