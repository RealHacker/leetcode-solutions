from collections import defaultdict

class Solution(object):
    def getTable(self, num, k):
        last = 0
        result = []
        while k:
            _max = max(num[last:len(num)-k+1])
            last = last + num[last:].index(_max)+1
            result.append(_max)
            k-=1

        return result

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        for n1 in range(min(k, len(nums1))+1):
            n2 = k - n1
            
            if n2 > len(nums2): continue
            r1 = self.getTable(nums1, n1)
            r2 = self.getTable(nums2, n2)

            r = []
            while r1 or r2:
                if not r1:
                    r = r+r2
                    break
                elif not r2:
                    r = r + r1
                    break
                else:
                    if r1>=r2:
                        r.append(r1[0])
                        r1.pop(0)
                    else:
                        r.append(r2[0])
                        r2.pop(0)
            # an elegant one-liner
            r = [max(r1, r2).pop(0) for _ in r1+r2]
            results.append(r)
        return max(results)

        

        
        
            