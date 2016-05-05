from collections import Counter
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        counter = Counter()
        max = 0
        maxnum = 0
        for num in nums:
            counter[num]+=1
            if counter[num]>max:
                max = counter[num]
                maxnum = num
        return maxnum
