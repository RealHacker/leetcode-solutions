import math
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        top1 = [None, 0]
        top2 = [None, 0]
        for num in nums:
            if top1[0] == num:
                top1[1] += 1
            elif top2[0] == num:
                top2[1] += 1
            elif top1[0] is None or top1[1]<=0:
                top1 = [num, 1]
            elif top2[0] is None or top2[1]<=0:
                top2 = [num, 1]
            else:
                top1[1] -=1
                top2[1] -=1
        top1[1]=0
        top2[1]=0
        for num in nums:
            if num==top1[0]:
                top1[1]+=1
            elif num==top2[0]:
                top2[1]+=1

        result = []
        if not top1[0] is None and top1[1]>math.floor(len(nums)/3.0):
            result.append(top1[0])
        if not top2[0] is None and top2[1]>math.floor(len(nums)/3.0):
            result.append(top2[0])
        
        return result
