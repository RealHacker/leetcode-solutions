# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict
import fractions
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points: return 0
        sets = []
        _max = 1
        for point in points:
            d = defaultdict(list)
            visited = set()
            for s in sets:
                if point in s:
                    visited = visited&s
            same = [point]
            for p in points:
                if p is point: continue
                if p in visited: continue
                if p.x==point.x and p.y==point.y:
                    same.append(p)
                    continue
                gcd = fractions.gcd(p.y-point.y, p.x-point.x)
                f = (p.y-point.y)/gcd, (p.x-point.x)/gcd
                d[f].append(p)
                
            _max = max(_max, len(same))
            for fr in d:
                s = set(d[fr]+same)
                sets.append(s)
                if len(d[fr])+len(same)>_max:
                    _max = len(d[fr])+len(same)
        return _max
                    
