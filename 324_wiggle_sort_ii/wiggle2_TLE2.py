class Solution(object):
    def partition(self, nums, head, tail):
        # returns a (from, to) interval for the pivot value
        pivot = nums[tail]
        i=head
        while i<=tail:
            if nums[i]==pivot:
                i+=1
            elif nums[i]<pivot:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
                i += 1
            else:
                nums[tail], nums[i] = nums[i], nums[tail]
                tail -= 1
        return (head, tail)
                
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 3-way partition the nums array 
        h, t = 0, len(nums)-1
        mid = len(nums)/2
        while True:
            k1, k2 = self.partition(nums, h, t)
            if mid>k2:
                h = k2+1
            elif mid<k1:
                t = k1-1
            else:
                break
            
        
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
                # k = idx
                # while nums[k]==nums[i-1]:
                #     k+=1
                # nums[k], nums[idx] = nums[idx], nums[k]
                nums[i] = nums[idx]
            
        
                    
