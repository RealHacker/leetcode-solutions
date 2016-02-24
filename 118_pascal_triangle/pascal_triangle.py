class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        rows = []
        for i in range(numRows):
            row = [1]
            for j in range(i/2):
                row.append(rows[-1][j]+rows[-1][j+1])
            if i and i%2:
                row = row + list(reversed(row))
            else:
                row = row + list(reversed(row[:-1]))
            rows.append(row)
        return rows
