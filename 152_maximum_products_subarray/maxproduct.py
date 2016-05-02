class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_product =  -sys.maxint
        min_positive = 1
        min_negative = - sys.maxint
        
        partial = 1
        for num in nums:
            partial = partial*num
            if partial>0:
                max_product = max(max_product, partial/min_positive)
                if partial<min_positive:
                    min_positive = partial
            elif partial<0:
                if min_negative==-sys.maxint:
                    max_product = max(max_product, partial)
                else:
                    max_product = max(max_product, partial/min_negative)
                if partial>min_negative:
                    min_negative = partial
            else:
                max_product = max(max_product, 0)
                partial = 1
                min_positive = 1
                min_negative = - sys.maxint
        return max_product
                
