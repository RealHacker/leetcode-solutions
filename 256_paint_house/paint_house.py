import sys
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        self.costs = costs
        self.memo = {}
        if not costs:
            return 0
        return min(self.recurse(0, 0), self.recurse(0, 1), self.recurse(0, 2))
        
    def recurse(self, start_index, color):
        if start_index==len(self.costs):
            return 0
        if (start_index, color) not in self.memo:
            cost = self.costs[start_index][color]
            _min = sys.maxint
            for c in [0,1,2]:
                if c!=color:
                    _min = min(_min, self.recurse(start_index+1, c))
            self.memo[(start_index, color)] = cost+_min
        return self.memo[(start_index, color)]
        
                
        
