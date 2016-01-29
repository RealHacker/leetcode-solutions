from collections import OrderedDict
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.od = OrderedDict()
        s = sorted(candidates, reverse=True)
        for num in s:
            if num in self.od:
                self.od[num]+=1
            else:
                self.od[num]=1
        self.nums = self.od.keys()
        self.table = {}
        result = self.buildTable(0, target)
        if not result:
            return []
        else:
            return [sorted(r) for r in result]
        
    def buildTable(self, idx, target):
        if target==0:
            return [[]]
        if target!=0 and idx==len(self.nums):
            return None
        if (idx, target) in self.table:
            return self.table[(idx, target)]
        
        if target<self.nums[idx]:
            results = self.buildTable(idx+1, target)
        else:
            results = []
            without = self.buildTable(idx+1, target)
            if without:
                results += without
            cnt = 1
            while cnt*self.nums[idx]<=target and cnt<=self.od[self.nums[idx]]:
                r = self.buildTable(idx+1, target-cnt*self.nums[idx])
                if r is not None:
                    results += [[self.nums[idx]]*cnt + rr for rr in r]
                cnt+=1
            if not results:
                results = None
        self.table[(idx, target)]=results
        return results
                
            
