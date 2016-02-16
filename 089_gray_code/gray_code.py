class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        num = 0
        while True:
            for i in range(n):
                m = 1<<i
                if num^m not in ret:
                    num = num^m
                    ret.append(num)
                    break
            else:
                break
        return ret
