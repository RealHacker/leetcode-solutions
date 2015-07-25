class Solution:
    def insort(self, point): # used to insert into sorted self.heights
        for i,height in enumerate(self.heights):
            if height[0] > point[1]:
                break
        self.heights.insert(i, (point[1], point[3]))

    def remove(self, point): # used to remove from self.heights
        for i, height in enumerate(self.heights):
            if height[1] == point[3]:
                break
        del self.heights[i]

    def getSkyline(self, buildings):
        buildings = sorted(buildings, cmp=lambda x,y: x[0]-y[0])

        # points is a list, with elements like 
        # (x_coordinate, y_coordinate, 
        # 'L'/'R' (building left/right side),
        # index_of_point_in_points)
        points = []

        # heights is a list of (point_height, point_index)
        self.heights = [(0,-1)]

        for i, building in enumerate(buildings):
            L, R, H = building
            points.append((L, H, 'L', i))
            points.append((R, H, 'R', i))

        # sort the points:
        # 1. First by x coordinate
        # 2. Then for points of same x, 
        #   put all L points after R points (descend -> ascend)
        # 3. For L points, sort by y, ascending
        # 4. For R points, sort by y, descending
        def point_cmp(x, y):
            if x[0] != y[0]:
                return x[0]-y[0]
            if x[2] != y[2]:
                return 1 if x[2]=='L' else -1
            if x[2] == 'L':
                return x[1]-y[1]
            else:
                return y[1]-x[1]

        points = sorted(points, cmp = point_cmp)

        results = []
        for point in points:
            if point[2] == 'L':
                # if higher than highest
                if point[1] > self.heights[-1][0]:
                    # put at the top of stack
                    self.heights.append((point[1], point[3]))
                    # remove dups
                    if results and point[0] == results[-1][0]:
                        results[-1][1] = point[1]
                    else:
                        # add a point to result
                        results.append([point[0], point[1]])            
                else:
                    self.insort(point)  
            else:
                if point[1] == self.heights[-1][0] and point[3] == self.heights[-1][1]:
                    self.heights.pop()
                    if results and point[0] == results[-1][0]:
                        results[-1][1] = self.heights[-1][0]
                    else:
                        results.append([point[0], self.heights[-1][0]])
                else:
                    self.remove(point)
        
        i = 1
        while i<len(results):
            if results[i-1][1] == results[i][1]:
                del results[i]
            else:
                i += 1
            
        return results
