from collections import defaultdict
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        edges = defaultdict(list)
        pointed_at = [0]*len(ratings)
        candies = [1]*len(ratings)
        
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1]:
                edges[i].append(i+1)
                pointed_at[i+1]=1
            elif ratings[i]>ratings[i+1]:
                edges[i+1].append(i)
                pointed_at[i]=1

        for i in range(len(ratings)):
            if pointed_at[i]==0:
                stack = [(1, i)]
                while stack:
                    v, p = stack.pop(0)
                    candies[p] = v if v>=candies[p] else candies[p]
                    for edge in edges[p]:
                        stack.insert(0, (v+1, edge))
        return sum(candies)
