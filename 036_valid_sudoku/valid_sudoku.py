class Solution(object):
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    map_row = [{} for _ in xrange(9)]
    map_col = [{} for _ in xrange(9)]
    map_cell = [[{} for _ in xrange(3)] for __ in xrange(3)]
    for i in xrange(9):
        for j in xrange(9):
            char = board[i][j]
            if char == '.': continue
            if char in map_row[i]: return False
            else: map_row[i][char] = [i,j]
            if char in map_col[j]: return False
            else: map_col[j][char] = [i,j]
            if char in map_cell[i/3][j/3]: return False
            else: map_cell[i/3][j/3][char] = [i,j]
    return True
