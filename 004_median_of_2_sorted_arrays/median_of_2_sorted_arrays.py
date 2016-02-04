class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
                total = len(nums1) + len(nums2)
                isEven = (total%2==0)
                idx = total/2 if not isEven else total/2-1
                n1, n2 = 0,0
                while True:
                        if not nums1:
                                if isEven:
                                        n1, n2 = nums2[idx], nums2[idx+1]
                                else:
                                        n1, n2 = nums2[idx], nums2[idx]
                                break
                        elif not nums2:
                                if isEven:
                                        n1, n2 = nums1[idx], nums1[idx+1]
                                else:
                                        n1, n2 = nums1[idx], nums1[idx]
                                break
                        elif idx == 0:
                                if isEven:
                                        a = [nums1[0], nums2[0]]
                                        if len(nums1)>1:
                                                a.append(nums1[1])
                                        if len(nums2)>1:
                                                a.append(nums2[1])
                                        a.sort()
                                        n1, n2 = a[0], a[1]
                                else:
                                        n1 = min(nums1[0], nums2[0])
                                        n2 = n1
                                break
                        else:
                                half1 = len(nums1)/2 if len(nums1)%2==0 else len(nums1)/2+1
                                half2 = len(nums2)/2 if len(nums2)%2==0 else len(nums2)/2+1
                                if idx/2<half1:
                                        half1 = idx/2
                                        half2 = idx - half1
                                else:
                                        half2 = idx/2
                                        half1 = idx - half2
                                if nums1[half1-1]<=nums2[half2-1]:
                                        nums1 = nums1[half1:]
                                        idx = idx-half1
                                else:
                                        nums2 = nums2[half2:]
                                        idx = idx-half2
                                
                return (n1 +n2)*0.5   
                                
                
