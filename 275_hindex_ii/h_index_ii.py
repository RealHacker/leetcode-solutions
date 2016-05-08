class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        if citations[0]>=len(citations):
            return len(citations)
        start = 0
        end = len(citations)-1
        citations = list(reversed(citations))
        while True:
            middle = (start+end)/2
            if citations[middle]>=(middle+1):
                start = middle
            else:
                end = middle-1
            if start==end:
                if citations[start]>=start+1:
                    return start+1
                else:
                    return 0
                
            if start+1==end:
                if citations[end]>=end+1:
                    return end+1
                elif citations[start]>=start+1:
                    return start+1
                else:
                    return 0
