from collections import defaultdict
from itertools import product
import re
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        self.s = ''.join([c for c in input if c!=" "])
        self.items = re.findall("\+|\-|\*|[0-9]+", self.s)
        l = len(self.items)
        self.memo = defaultdict(set)
        self.visit(0, l-1)
        return list(self.memo[(0, l-1)])

    def visit(self, left, right):
    	if (left, right) in self.memo:
    		return self.memo[(left, right)]
    	if left == right:
    		self.memo[(left, right)]=[int(self.items[left])]
    		return self.memo[(left, right)]
    	else:
    		_set = []
    		operator_idx = left + 1
    		while operator_idx < right:
    			operator = self.items[operator_idx]
    			set1 = self.visit(left, operator_idx-1)
    			set2 = self.visit(operator_idx+1, right)
    			for a, b in product(set1, set2):
    				if operator == '+':
    					_set.append(a+b)
    				elif operator == '-':
    					_set.append(a-b)
    				elif operator == '*':
    					_set.append(a*b)
    			operator_idx += 2
    		self.memo[(left, right)] = _set
    		return _set

