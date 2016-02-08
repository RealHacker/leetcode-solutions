class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ascending = []
        last = 0
        for i, h in enumerate(height):
            if h>last:
                ascending.append((i, h))
                last = h
        descending = []
        last = 0
        for i, h in enumerate(reversed(height)):
            if h>last:
                descending.append((len(height)-1-i, h))
                last = h
        max_water = 0
        for left, lh in ascending:
            for right, rh in descending:
                if left>=right:
                    break
                water = min(lh, rh) * (right-left)
                if water >max_water:
                    max_water = water
                if rh>=lh:
                    break
        return max_water
