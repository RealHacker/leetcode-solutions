class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = 0
        y = 0
        xx = len(matrix)-1
        yy = len(matrix[0])-1
        rows = xx+1
        cols = yy+1
        
        while True:
            row = matrix[x][y:yy+1]
            py = bisect.bisect_left(row, target)
            if py<len(row) and row[py]==target:
                return True
            if py==0:
                return False
            col = [matrix[r][y] for r in range(x, xx+1)]
            px = bisect.bisect_left(col, target)
            if px<len(col) and col[px]==target:
                return True
            if px==0:
                return False
            xx = x+px-1
            yy = y+py-1
            x = x+1
            y = y+1
            if x>xx or y>yy:
                return False
            
            
