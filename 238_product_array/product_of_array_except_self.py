class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        before = []
        after = []
        product = 1
        for num in nums:
            before.append(product)
            product = product * num
        product = 1
        for num in reversed(nums):
            after.append(product)
            product = product* num
        after = after[::-1]
        
        result = []
        for i in range(len(nums)):
            result.append(before[i]*after[i])
        return result
        
