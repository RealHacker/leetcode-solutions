class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxa = 0
        if not matrix:
            return 0
        vector = [0]* len(matrix[0])
        for r in matrix:
            for i, c in enumerate(r):
                if c == '0':
                    vector[i]=0
                else:
                    vector[i]+=1
	    print vector
            maxa = max(maxa, self.largestRectangleArea(vector[:]))
        return maxa
            
        
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

        return maxarea
