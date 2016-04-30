class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
        	return 0
        intervals = []
        current = 0
        bucket = None
        for i in range(1, len(ratings)):
        	if ratings[i]>ratings[current]:
        		if not bucket:
        			bucket = ("up", {"start":current, "end":None})
        		else:
        			if bucket[0]!='up':
        				bucket[1]['end']=i-1
        				intervals.append(bucket)
        				bucket = ("up", {"start":current, "end":None})
        	elif ratings[i]<ratings[current]:
        		if not bucket:
        			bucket = ("down", {"start":current, "end":None})
        		else:
        			if bucket[0]!='down':
        				bucket[1]['end']=i-1
        				intervals.append(bucket)
        				bucket = ("down", {"start":current, "end":None})
        	else:
        		if not bucket:
        			bucket = ("level", {"start":current, "end":None})
        		else:
        			if bucket[0]!='level':
        				bucket[1]['end']=i-1
        				intervals.append(bucket)
        				bucket = ("level", {"start":current, "end":None})
        	current = i

        if not bucket:
        	return 1
        else:
        	bucket[1]['end'] = len(ratings)-1
        	intervals.append(bucket)

        print intervals
        candies = []
        for i in range(len(ratings)):
        	candies.append(0)

        for interval in intervals:
        	if interval[0]=="level": 
        		continue
        	elif interval[0]=="up":
        		for j in range(interval[1]['start'], interval[1]['end']+1):
        			x = j-interval[1]['start']+1
        			candies[j] = max(candies[j], x)
        	elif interval[0]=="down":
        		for j in range(interval[1]['start'], interval[1]['end']+1):
        			x = interval[1]['end']-j+1
        			candies[j] = max(candies[j], x)
        least = sum([x if x else 1 for x  in candies ])
        return least