class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        deltas = [(0, 1),(1,0),(0,-1),(-1,0)]
        
        d_index = 0
        x, y = 0, 0
        counter = 0
        total = m*n
        result = []
        while True:
            if total==0:
                break
            #print x, y
            result.append(matrix[x][y])
            total -=1
            if (counter==n-1 or counter==n+m-2 or 
                counter==2*n+m-3 or counter==m*2+n*2-5):
                d_index=(d_index+1)%4
                if counter==m*2+n*2-5:
                    counter = 0
                    m = m-2
                    n = n-2
                    y = y+1
                    continue
            dx, dy = deltas[d_index]
            x += dx
            y += dy
            counter +=1
            
        return result
