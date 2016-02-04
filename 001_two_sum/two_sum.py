class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = [(i, nums[i]) for i in range(len(nums))]
        a.sort(key=operator.itemgetter(1))
        
        i = 0
        j = len(nums)-1
        while True:
            if i==j:
                print "should not happen"
                break
            sum = a[i][1]+a[j][1]
            if sum==target:
                break
            elif sum<target:
                i+=1
            else:
                j-=1
        return sorted([a[i][0]+1, a[j][0]+1])
