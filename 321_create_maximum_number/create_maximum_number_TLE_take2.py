from collections import defaultdict

class Solution(object):
    def translate(self, table, length):
        for c in table:
            poses = table[c]
            nexts = []
            for n in range(length):
                if not poses:
                    nexts.append(-1)                
                else:
                    if n<=poses[0]:
                        nexts.append(poses[0])
                    if n==poses[0]:
                        poses.pop(0)
            table[c] = nexts

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.len1 = len(nums1)
        self.len2 = len(nums2)
        self.table1 = defaultdict(list)
        self.table2 = defaultdict(list)

        for i,c in enumerate(nums1):
            self.table1[c].append(i)
        self.translate(self.table1, self.len1)

        for i,c in enumerate(nums2):
            self.table2[c].append(i)
        self.translate(self.table2, self.len2)

        # print self.table1, self.table2
        return self.recurse(0, 0, k)
        
    def recurse(self, i, j, k):
        if k==0: return []
        
        l1 = self.len1-(k-1-self.len2+j) if k-1>self.len2-j else self.len1
        l2 = self.len2-(k-1-self.len1+i) if k-1>self.len1-i else self.len2
        # print l1, l2, i,j,k

        maxv = -1
        maxitems = []
        for c in range(9, -1, -1):
            maxitems = []
            if self.table1[c] and i<self.len1 and self.table1[c][i]>=0 and self.table1[c][i]<l1:
                maxitems.append((0, self.table1[c][i]))
                
            if self.table2[c] and j<self.len2 and self.table2[c][j]>=0 and self.table2[c][j]<l2:
                maxitems.append((1, self.table2[c][j]))
                    
            if maxitems:
                # print maxitems
                maxv = c
                break

        maxresult = None
        for tag, idx in maxitems:
            if tag==0:
                result = self.recurse(idx+1, j, k-1)
            else:
                result = self.recurse(i, idx+1, k-1)
            if maxresult is None:
                maxresult = result
            elif len(maxresult)>0:
                m = 0
                while m<len(maxresult) and maxresult[m]==result[m]:
                    m+=1
                if m<len(maxresult) and maxresult[m]<result[m]:
                    maxresult = result
        #print [maxv] + maxresult
        return [maxv] + maxresult
        
        
            
        
        
            