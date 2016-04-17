import bisect
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
        minx, maxx = x, x+1
        miny, maxy = y, y+1
        
        lo, hi = 0, x
        while lo<hi:
            mid = (lo+hi)/2
            if any([c=='1' for c in image[mid]]):
                hi = mid
            else:
                lo = mid+1
        minx = hi
        
        lo, hi = x, xl
        while lo<hi:
            mid = (lo+hi)/2
            if any([c=='1' for c in image[mid]]):
                lo = mid+1
            else:
                hi = mid
        maxx = hi
        print minx, maxx
        lo, hi = 0, y
        while lo<hi:
            mid = (lo+hi)/2
            if any([image[i][mid]=='1' for i in range(minx, maxx)]):
                hi = mid
            else:
                lo = mid+1
        miny = hi
        
        lo, hi = y, yl
        while lo<hi:
            mid = (lo+hi)/2
            if any([image[i][mid]=='1' for i in range(minx, maxx)]):
                lo = mid+1
            else:
                hi = mid
        maxy = hi
        print miny, maxy
        return (maxx-minx)*(maxy-miny)
        
                    
                    
        
