from functools import partial
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def _cmp(prefix, n1, n2):
            if not n1:
                if not n2:
                    return 0
                else:
                    return _cmp("", prefix, n2)
            if not n2:
                return _cmp("", n1, prefix)
                
            if n1[0]<n2[0]:
                return -1
            elif n1[0]>n2[0]:
                return 1
            else:
                return _cmp(prefix+n1[0], n1[1:], n2[1:])
        numstrs = [str(num) for num in nums]
        numstrs.sort(cmp = partial(_cmp, ""))
        result = ""
        
        if numstrs[-1]=="0":
            return "0"
        for n in numstrs[::-1]:
            result += n
        
        return result
        
        
