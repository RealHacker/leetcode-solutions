class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # partition the nums into 2 halves, with left half < right half
        k1 = 0
        k2 = len(nums)-1
        while True:
            pos = k1
            for i in range(k1, k2):
                if nums[i]<nums[k2]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos+=1
            nums[k2], nums[pos] = nums[pos], nums[k2]
            if pos==len(nums)/2: 
                break
            elif pos<len(nums)/2:
                k1 = pos+1
            else:
                k2 = pos-1
        
        stack = []
        for i in range(1, len(nums)):
            if i%2==0:
                stack.append(nums[i])
                nums[i] = stack.pop(0)
            else:
                stack.append(nums[i])
                if len(nums)%2==0:
                    idx = len(nums)/2+i/2
                else:
                    idx = len(nums)/2+i/2+1
                k = idx
                while nums[k]==nums[i-1]:
                    k+=1
                nums[k], nums[idx] = nums[idx], nums[k]
                nums[i] = nums[idx]
            
        
                    
