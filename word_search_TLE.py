from collections import defaultdict
import functools
import copy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        d = defaultdict(list)
	for i in range(len(board)):
		for j in range(len(board[0])):
			d[board[i][j]].append((i, j))
	return self.recurse(word, d, None)

    def ajacent(self, pos1, pos2):
	i1, j1 = pos1
        i2, j2 = pos2
        if j1==j2 and (i1+1==i2 or i1-1==i2): return True
        if i1==i2 and (j1+1==j2 or j1-1==j2): return True
        return False

    def recurse(self, word, d, last):
	if not word:
		return True
	if not last:
		choices = d[word[0]]
	else:
		choices = filter(functools.partial(self.ajacent, last), d[word[0]])
	if not choices:
		return False
        ret = False
	for c in choices:
		newd = copy.deepcopy(d)
                newd[word[0]].remove(c)
		ret = ret or self.recurse(word[1:], newd, c)
		if ret:
			break
	return ret
