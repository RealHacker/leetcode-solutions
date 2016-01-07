from bisect import bisect_left

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		isOdd = (len(nums1)+len(nums2))%2==1
		if isOdd:
			half = (len(nums1)+len(nums2))//2
		else:
			half = (len(nums1)+len(nums2))/2
		a1, a2 = nums1, nums2
		count = 0
		rest = half
		while True:
			print a1, a2
			idx1 = rest/2
			if not a1 or not a2:
				break

			if idx1 >= len(a1):
				idx1 = len(a1)-1
			num = a1[idx1]
			idx2 = bisect_left(a2, num)

			newcount = idx2+idx1+count
			if newcount==half:
				nexts = []
				if idx1 < len(a1):
					nexts.append(a1[idx1])
				if idx2 < len(a2):
					nexts.append(a2[idx2])
				next = min(nexts)
				if isOdd:
					return next
				else:
					firsts = []
					if idx1 > 0:
						firsts.append(a1[idx1-1])
					if idx2 > 0:
						firsts.append(a2[idx2-1])
					first = max(firsts)
					return (first+next)*0.5
			elif newcount > half:
				a1, a2 = a2, a1
			else:
				count = newcount
				rest = half - count
				a1, a2 = a2[idx2:], a1[idx1:]
		a = a1 if a1 else a2
		if isOdd:
			return a[rest]
		else:
			return (a[rest-1]+a[rest])*0.5