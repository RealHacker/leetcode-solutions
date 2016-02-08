class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {
            '1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
            '0':" ",
        }
        if not digits:
            return []
        from itertools import product
        l = [c for c in map[digits[0]]]
        for digit in digits[1:]:
            l = product(l, map[digit])
            l = [''.join(item) for item in l]
        result = l
        return result
