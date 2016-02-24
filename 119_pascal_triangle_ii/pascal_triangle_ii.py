class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex ==0:
            return [1]
        row = [1,1]
        if rowIndex==1:
            return row
        for i in range(2, rowIndex+1):
            for j in range(len(row)-1):
                row[j]=row[j]+row[j+1]
            row[j+1]=1
            row.insert(0,1)
        return row
        
