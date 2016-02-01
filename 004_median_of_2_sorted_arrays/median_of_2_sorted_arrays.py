class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		if not nums1:
		    last = nums2
		elif not nums2:
		    last = nums1
		else:
			while True:
			    print nums1, nums2
			    if len(nums1)<=2 and len(nums2)<=2:break
			    median1 = nums1[len(nums1)/2]
			    median2 = nums2[len(nums2)/2]
			    if len(nums1)<len(nums2):
			    		half = len(nums1)/2
			    	else:
			    		half = len(nums2)/2
			    if median1<median2:
			        nums1 = nums1[half:]
			        nums2 = nums2[:-half]
			    elif median1>median2:
			        nums1 = nums1[:-half]
			        nums2 = nums2[half:]
			    else:
			    	if len(nums1)%2 or len(nums2)%2:
			    		return median1
			    	else:
			    		return (median1 + max(nums1[len(nums1)/2-1], nums2[len(nums2)/2-1])) * 0.5
			last = sorted(nums1+nums2)
		print last
		if len(last)%2:
		    return last[len(last)/2]
		else:
		    return (last[len(last)/2-1]+last[len(last)/2])*0.5