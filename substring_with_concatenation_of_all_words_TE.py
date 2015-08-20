import itertools
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
    	if not s or not words:
    		return []
    	d = {}
    	wordlen = len(words[0])
    	for word in words:
    		poses = []
    		start = 0
    		while True:
    			idx = s.find(word, start)
    			if idx < 0:
    				break
    			poses.append(idx)
    			start = idx+wordlen
    		d[word] = poses
    	tuple_list = [d[word] for word in words]
    	combs =  itertools.product(*tuple_list)
    	starts = []
    	for comb in combs:
    		comb = sorted(comb)
    		valid = True
    		for i in range(1, len(comb)):
    			if comb[i] != comb[i-1]+wordlen:
    				valid = False
    				break
    		if valid:
    			starts.append(comb[0])
    	return starts
        
s = "barfoothefoobarman"
words = ["foo", "bar"]
print Solution().findSubstring(s, words)