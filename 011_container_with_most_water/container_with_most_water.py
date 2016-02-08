class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        _max = 0
        while l<r:
            _max = max(_max, min(height[l], height[r])*(r-l))
            if height[l]<=height[r]:
                while l<r and height[l+1]<=height[l]: l+=1
                l+=1
            else:
                while l<r and height[r-1]<=height[r]: r-=1
                r-=1
        return _max
