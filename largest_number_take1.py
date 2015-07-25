class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted([str(num) for num in nums])
        result = ""
        while nums:
            num = self.pickone(nums, None)
            result += num
            nums.remove(num)
        if result[0] == '0':
            result = '0'
        return result
        
    def pickone(self, nums, memo):
        if len(nums) == 1:
            return nums[0]
            
        candidates = []
        c = nums[-1][0]
        idx = len(nums)-1
        while nums[idx][0]==c and idx>=0:
            candidates.append(nums[idx])
            idx -= 1
        
        if len(candidates) == 1:
            return candidates[0]
        else:
            if not memo:
                memo = c
            candidates = sorted([candidate[1:] for candidate in candidates])
            if '' in candidates:
                while '' in candidates:
                    candidates.remove('')
                if not candidates:
                    return c
                max = self.pickone(candidates, memo)
                if memo > max:
                    return c
                else:
                    return c+max
            else:
                return c + self.pickone(candidates, memo)


solution = Solution()
print solution.largestNumber([4993,9779,9200])
