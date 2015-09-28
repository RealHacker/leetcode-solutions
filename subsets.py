class Solution(object):

    def subsets(self, nums):

        """

        :type nums: List[int]

        :rtype: List[List[int]]

        """

        import itertools

        result = []

        for i in range(len(nums)+1):

            for combi in itertools.combinations(nums, i):

                result.append(sorted(combi))

        return result
