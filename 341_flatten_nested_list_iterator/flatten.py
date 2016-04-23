# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = self.flatten(nestedList)
        self.index = 0
        
    def flatten(self, nestedList):
        result = []
        for item in nestedList:
            if item.isInteger():
                result.append(item.getInteger())
            else:
                result += self.flatten(item.getList())
        return result

    def next(self):
        """
        :rtype: int
        """
        if self.index >= len(self.list):
            return None
        v = self.list[self.index]
        self.index += 1
        return v

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
