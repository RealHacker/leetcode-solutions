class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        results = set()
        for i in range(len(nums)-2):
            first = nums[i]
            t = target-first
            head = i+1
            if head>=len(nums):break
            tail = len(nums)-1
            while head<tail:
                current = nums[head]+nums[tail]
                if current>t:
                    tail -=1
                elif current<t:
                    head +=1
                else:
                    results.add((first, nums[head], nums[tail]))
                    tail -=1
                    head +=1
        return list(results)
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = set()
        for i in range(len(nums)-3):
            a = nums[i]
            for b,c,d in self.threeSum(nums[i+1:], target-a):
                results.add((a, b, c, d))
        return list(results)
        
