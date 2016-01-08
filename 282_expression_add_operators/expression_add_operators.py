class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
	self.num = num
	self.mul_dict = {(i,i):[(num[i], int(num[i]))] for i in range(len(num))}
	self.add_dict = {}
	for k in range(len(num)):
		self.recurse_times(0, k)
	results = self.recurse(0, len(num)-1)

	ret = []
	for result in results:
		if result[1]==target and not result[0].startswith("-"):
			ret.append(result[0])
	return ret	
	
    def recurse_times(self, start, end):
	if (start, end) in self.mul_dict:
		return self.mul_dict[(start, end)]
	results = []
	for i in range(start, end+1):
		if i>start and self.num[start]=='0': continue
		left = int(self.num[start:i+1])
		if i<end:	
			rights = self.recurse_times(i+1, end)
			for s, val in rights:
				results.append((self.num[start:i+1]+"*"+s, val*left))
		else:
			results.append((self.num[start:i+1], left))
	self.mul_dict[(start, end)]= results
	return results	

    def recurse(self, start, end):
	if (start, end) in self.add_dict:
		return self.add_dict[(start, end)]
	results = []
	for i in range(start, end+1):
		lefts = self.mul_dict[(start, i)]
		if i<end:
			rights = self.recurse(i+1, end)
			for left, vleft in lefts:
				for right, vright in rights:
					if right.startswith("-"):
						results.append((left+right, vleft+vright))
						results.append(("-"+left+right, -vleft+vright))
					else:
						results.append((left+"+"+right, vleft+vright))
						results.append(("-"+left+"+"+right, -vleft+vright))
		else:
			results.extend(lefts)
			results.extend([("-"+s, -v) for (s,v) in lefts])
	self.add_dict = results
	return results
	
