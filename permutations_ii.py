from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        self.counter = Counter(nums)
        self.result = []
        self.recurse(self.counter, [])
        return self.result
        
    def recurse(self, counter, partial, last=None):
        if len(counter.keys())==1:
            final = counter.keys()[0]
            self.result.append(partial +[final]*counter[final])
        else:
            for key in counter.keys():
                if last is not None and key==last: continue
                for i in range(1, counter[key]+1):
                    _counter = counter.copy()
                    _counter[key]-=i
                    if _counter[key]==0: 
                        del _counter[key]
                    self.recurse(_counter, partial+[key]*i, key)
        
                
            
