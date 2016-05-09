class Solution(object):
    def getMedian(self, is_odd, array):
        if is_odd:
            return array[1]
        else:
            return  (array[0]+array[1])*0.5
    def getMax(self, a1, i1, a2, i2):
        if i1 >= len(a1) or i1<0:
            return a2[i2]
        if i2 >=len(a2) or i2 <0:
            return a1[i1]
        return max(a1[i1], a2[i2])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        is_odd = (len(nums1) + len(nums2))%2>0

        half = (len(nums1) + len(nums2))/2+1

        if not nums1:
            a = [ nums2[len(nums2)/2-1],nums2[len(nums2)/2] ]
            return self.getMedian(is_odd, a)

        left = 0 
        right = len(nums2)
        while True:
            idx = (left + right)/2
            rest = half-(idx+1)
            if rest > len(nums1):
                left = idx +1
                continue
            if nums2[idx]>=nums1[rest-1]:
                if rest == len(nums1) or nums2[idx]<=nums1[rest]:
                    second_to_last = self.getMax(nums1, rest-1, nums2, idx-1)
                    return self.getMedian(is_odd, [second_to_last, nums2[idx]])
                else:
                    right = idx-1
                    continue
            else:
                if idx == len(nums2)-1 or nums2[idx+1]>=nums1[rest-1]:
                    second_to_last = self. getMax(nums1, rest-2, nums2, idx)
                    return self.getMedian(is_odd, [second_to_last, nums1[rest-1]])
                else:
                    left = idx +1
                    continue




