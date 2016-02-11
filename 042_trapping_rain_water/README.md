Water can only be hold between peaks. If you look at the pattern of pair of peaks that hold water, you can see that:

- From left to the highest peaks, the peaks that form alleys are in ascending order, and the peak at i is the largest for 0-i.
- From the highest peak to the right, the peaks are in descending order, and the peak at j is the largest from j to the end.

So the problem is reduced to 2 passes over the heights array:


1. Start from the left, for each pos i, if a[i] > maxheight up to i, put i in lefts.
2. Start from the right, for each pos j, if a[j] > maxheight from j to end, put j in rights.

Now we can get the pair of peaks that form valleys (mind duplicate pairs with same heights). Calculate the amount of water between 2 peaks is straightforward. 