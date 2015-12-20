class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0]*len(nums)
        self.sums = [0]*(len(nums)+1)
        
        for i, num in enumerate(nums):
            self.update(i, num)
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        old = self.nums[i]
        self.nums[i]=val
        diff = val-old
        i+=1
        while i<len(self.sums):
            self.sums[i]+=diff
            i += i&(-i)
        
    def sum(self, i):
        sum = 0
        i+=1
        while i!=0:
            sum+= self.sums[i]
            i -= i&(-i)
        return sum
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j)-self.sum(i-1)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
