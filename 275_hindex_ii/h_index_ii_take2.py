class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        i = 0
        j = len(citations)-1
        
        while True:
            mid = (i+j)/2
            if citations[mid]<len(citations)-mid:
                i=mid+1
                if i>j:
                    return 0
            else:
                j=mid
                if i==j:
                    break
        
        return len(citations)-i
