class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # topological sort
        courses = set(list(range(numCourses)))
        result = []
        while courses:
            independants = courses-set([p[0] for p in prerequisites])
            # print independants
            for independant in independants:
                result.append(independant)
                courses.remove(independant)
            if not independants:
                return []
            for k in range(len(prerequisites)-1, -1, -1):
                x, y = prerequisites[k]
                if y in independants:
                    del prerequisites[k]
        return result
