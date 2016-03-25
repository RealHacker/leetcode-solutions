class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        results = [0,1]
        if num<2:
            return results[:num+1]
        threshold = 2
        counter = 0
        for i in range(2,num+1):
            results.append(results[i-threshold]+1)
            counter += 1
            if counter==threshold:
                threshold*=2
                counter=0
        return results
            
