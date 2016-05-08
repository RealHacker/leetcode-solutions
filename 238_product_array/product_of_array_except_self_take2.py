class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        # first pass from front to back
        product = 1
        for num in nums:
            product = product*num
            result.append(product)
        # second pass from back to front
        product = 1
        for i in range(len(nums)-1, -1, -1):
            if i>0:
                result[i] = result[i-1]*product
            else:
                result[i] = product
            product = product* nums[i]
        return result
            
