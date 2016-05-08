class Solution:

    # @param {integer[]} nums

    # @param {integer} k

    # @return {integer[]}

    def maxSlidingWindow(self, nums, k):

        if not nums:

            return []

        left = 0

        right = k

        maxes = []

        l = len(nums)

        

        while right <= l:

            window = nums[left:right]

            maxes.append(max(window))

            left += 1

            right += 1

        return maxes
