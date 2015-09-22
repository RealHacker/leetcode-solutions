# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.cache = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache:
            return self.cache
        if not self.it.hasNext():
            return None
        self.cache = self.it.next()
        return self.cache
        
    def next(self):
        """
        :rtype: int
        """
        if self.cache:
            temp = self.cache
            self.cache = None
            return temp
        else:
            return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cache:
            return True
        return self.it.hasNext()
