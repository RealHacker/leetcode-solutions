class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        areas = {}
        sorted_height = sorted(list(set(height)))
        lh = len(height)
        for i in range(lh):
            h = height[lh-1-i]
            areas[lh-1-i] = {}
            j = 0
            while sorted_height[j] <= h:
                hh = sorted_height[j]
                if i == 0:
                    addition = 0
                else:
                    addition = areas[lh-i][hh] if hh in areas[lh-i] else 0
                areas[lh-1-i][hh] = hh + addition
        max = 0
        for i in range(lh):
            if areas[i][height[i]] > max:
                max = areas[i][height[i]]
        return max
