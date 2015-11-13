class NumArray(object):

    def __init__(self, nums):

        """

        initialize your data structure here.

        :type nums: List[int]

        """

        self.nums = nums

        self.sums = [0]

        sum = 0

        for num in self.nums:

            sum += num

            self.sums.append(sum)

        

    def sumRange(self, i, j):

        """

        sum of elements nums[i..j], inclusive.

        :type i: int

        :type j: int

        :rtype: int

        """

        if i>j: return 0

        elif i == j: return self.nums[i]

        else:

            if j+1 <len(self.sums):

                return self.sums[j+1]-self.sums[i]

            else:

                return self.sums[-1] - self.sums[i]
