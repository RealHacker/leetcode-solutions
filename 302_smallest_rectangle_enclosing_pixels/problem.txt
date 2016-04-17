class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image:
            return 0
        # BFS from x, y to find the boundaries
        xl = len(image)
        yl = len(image[0])
        minx, maxx = x, x
        miny, maxy = y, y
        
        visited = set((x, y))
        q = [(x,y)]
        
        # Loop for BFS 
        while q:
            xx, yy = q.pop(0)
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]
            for dx, dy in directions:
                # print xx+dx, yy+dy
                if (0<=xx+dx<xl and 0<=yy+dy<yl and image[xx+dx][yy+dy]=='1' 
                    and (xx+dx, yy+dy) not in visited):
                    q.append((xx+dx, yy+dy))
                    visited.add((xx+dx, yy+dy))
                    minx = min(minx, xx+dx)
                    maxx = max(maxx, xx+dx)
                    miny = min(miny, yy+dy)
                    maxy = max(maxy, yy+dy)
        #     print q
        # print minx, maxx, miny, maxy
        return (maxx-minx+1)*(maxy-miny+1)
        
                    
                    
        
