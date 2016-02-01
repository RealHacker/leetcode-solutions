class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        nums = sorted(nums)
        n = 0
        while n<len(nums) and nums[n]<=0: n+=1
        if n==0: return []
        results = set()
        for i in range(n):
            first = nums[i]
            target = -first
            head = i+1
            if head>=len(nums):break
            tail = len(nums)-1
            while head<tail:
                current = nums[head]+nums[tail]
                if current>target:
                    tail -=1
                elif current<target:
                    head +=1
                else:
                    results.add((first, nums[head], nums[tail]))
                    tail -=1
                    head +=1
        return list(results)
        
