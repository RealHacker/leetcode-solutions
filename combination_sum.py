class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        q = [(target, [])]
        candidates = sorted(candidates)
        result = []
        while q:
            num, history = q.pop(0)
            if num == 0:
                result.append(history)
            else:
                if not history:
                    if num<candidates[0]:
                        continue
                    idx = 0
                else:
                    idx = history[-1][0]+1
                    
                if idx>=len(candidates):
                    continue
                if candidates[idx]>num:
                    continue
                while True:
                    cnt = 1
                    while num>=cnt*candidates[idx]:
                        newnum = num-cnt*candidates[idx]
                        newhistory = history[:]
                        newhistory.append((idx, cnt))
                        q.append((newnum, newhistory))
                        cnt+=1
                    idx += 1
                    if idx>=len(candidates) or candidates[idx]>num:
                        break
        ret = []
        for r in result:
            l = []
            for idx, cnt in r:
                l.extend([candidates[idx]]*cnt)
            ret.append(l)
            
        return ret
