class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diffs = [gas[i]-cost[i] for i in range(len(gas))]
        least = 0
        min_index = 0
        sum = 0
        for i, diff in enumerate(diffs):
            if sum <least:
                least = sum
                min_index = i
            sum = sum+diff
        if sum<0:
            return -1
        return min_index
