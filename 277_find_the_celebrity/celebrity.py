# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        x = 0
        for i in xrange(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in xrange(x)):
            return -1
        if any(not knows(i, x) for i in xrange(n)):
            return -1
        return x
        
