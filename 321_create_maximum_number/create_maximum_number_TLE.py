class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==0: return []
        
        triples = []
        if len(nums2)>=k-1:
            candidates1 = nums1
        else:
            reserve = k-1-len(nums2)
            candidates1 = nums1[:-reserve]
        for i,c in enumerate(candidates1):
            triples.append((0, i, c))
        
        if len(nums1)>=k-1:
            candidates2 = nums2
        else:
            reserve = k-1-len(nums1)
            candidates2 = nums2[:-reserve]
        for i,c in enumerate(candidates2):
            triples.append((1, i, c))
            
        maxitems = []
        maxv = -1
        for tag, idx, v in triples:
            if v>maxv:
                maxv = v
                maxitems = [(tag, idx, v)]
            elif v==maxv:
                maxitems.append((tag, idx, v))
        
        maxresult = None
        for tag, idx, v in maxitems:
            if tag==0:
                result = self.maxNumber(nums1[idx+1:], nums2, k-1)
            else:
                result = self.maxNumber(nums1, nums2[idx+1:], k-1)
            if maxresult is None:
                maxresult = result
            elif len(maxresult)>0:
                i = 0
                while i<len(maxresult) and maxresult[i]==result[i]:
                    i+=1
                if i<len(maxresult) and maxresult[i]<result[i]:
                    maxresult = result
        return [maxv] + maxresult
        
        
            
        
        
            