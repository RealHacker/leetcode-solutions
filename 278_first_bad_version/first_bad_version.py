# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            if start==end:
                return start
            candidate = (start+end)/2
            if isBadVersion(candidate):
                end = candidate
            else:
                start = candidate+1
        
