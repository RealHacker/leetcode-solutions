class Solution(object):

    # def largestRectangleArea(self, height):
    #     height.append(0)
    #     stack = [-1]
    #     ans = 0
    #     for i in xrange(len(height)):
    #         while height[i] < height[stack[-1]]:
    #             h = height[stack.pop()]
    #             w = i - stack[-1] - 1
    #             ans = max(ans, h * w)
    #         stack.append(i)
    #     height.pop()
    #     return ans


    def largestRectangleArea(self, heights):

        """

        :type heights: List[int]

        :rtype: int

        """

        heights.insert(0,0)

        heights.append(0)

        stack = []

        maxarea = 0

        for i, height in enumerate(heights):

            if not stack or heights[stack[-1]]<=height:

                stack.append(i)

            else:

                while stack and heights[stack[-1]]>height:

                    maxarea = max(maxarea, heights[stack[-1]]*(i-stack[-2]-1))

                    stack.pop()

                stack.append(i)
        right = stack[-1]
        stack.pop()
        while len(stack)>1:
            offset = right-stack[-1]
            maxarea = max(maxarea, heights[stack[-1]]*offset)
            stack.pop()
            
        return maxarea

                    
