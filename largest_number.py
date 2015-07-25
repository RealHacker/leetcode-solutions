class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def ncmp(s1, s2):
            if s1+s2>s2+s1:
                return 1
            elif s1+s2==s2+s1:
                return 0
            else:
                return -1
        nums = sorted([str(num) for num in nums], cmp=ncmp)
        result = ""
        while nums:
            num = nums.pop()
            result += num
            
        if result[0] == '0':
            result = '0'
        return result
