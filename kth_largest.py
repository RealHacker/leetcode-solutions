class Solution:

    # @param {integer[]} nums

    # @param {integer} k

    # @return {integer}

    def findKthLargest(self, nums, k):

        import heapq

        return heapq.nlargest(k, nums)[k-1]	
