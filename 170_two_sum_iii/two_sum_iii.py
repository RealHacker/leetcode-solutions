from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.numbers = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.numbers[number]+=1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.numbers:
            m = value-n
            if m!=n and m in self.numbers:
                return True
            if m==n and self.numbers[n]>1:
                return True
        return False
                

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
