class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        results = []
        start = None
        for i, n in enumerate(nums):
            if start is None:
                start = n
                continue
            if n > nums[i-1]+1:
                if nums[i-1] == start:
                    results.append(str(start))
                else:
                    results.append("%d->%d"%(start, nums[i-1]))
                start = n
        if nums[i] == start:
            results.append(str(start))
        else:
            results.append("%d->%d"%(start, nums[i]))
        return results