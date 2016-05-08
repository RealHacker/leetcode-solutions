class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        corners = []
        for x1, x2, h in buildings:
            corners.append((x1, 0, h))
            corners.append((x2, 1, h))
      
        
        # sort the corners first by x, then by left/right
        corners.sort()
        
        # process the skyline
        skyline = []
        heights = []
        
        for x, isRight, h in corners:
            if not isRight:
                if not heights:
                    heights.append(h)
                    skyline.append([x, h])
                else:
                    idx = bisect.bisect(heights, h)
                    heights.insert(idx, h)
                    if idx==len(heights)-1:
                        if skyline and skyline[-1][0]==x:
                            skyline[-1][1]=h
                        else:
                            skyline.append([x, h])
            else:
                idx = bisect.bisect_left(heights, h)
                del heights[idx]
                if not heights:
                    skyline.append([x, 0])
                else:
                    if idx==len(heights):
                        if skyline and skyline[-1][0]==x:
                            skyline[-1][1]=heights[-1]
                        else:
                            skyline.append([x, heights[-1]])
            
        # compress the ys
        result = []
        i = 0
        while i<len(skyline):
            x, y = skyline[i]
            result.append((x, y))
            j = i+1
            while j<len(skyline) and skyline[j][1]==y:
                j+=1
            i = j
        
        return result
                    
                        
                    
                    
            
