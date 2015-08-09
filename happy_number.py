class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        appeared = set()
        appeared.add(n)
        while True:
            digits = [int(c) for c in str(n)]
            newval = sum([digit**2 for digit in digits])
            if newval ==1:
                return True
            if newval in appeared:
                return False
            appeared.add(newval)
            n = newval
