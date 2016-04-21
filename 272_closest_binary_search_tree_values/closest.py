# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import operator
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack = []
        node = root
        while node:
            if node.val<target:
                stack.append((node, 1))
                node = node.right
            else:
                stack.append((node, -1))
                node = node.left
                
        smaller = []
        greater = []

        for node, direction in stack[::-1]:
            if direction<0 and len(greater)<k:
                # still need more numbers > target
                greater.append(node.val)
                if len(greater)<k:
                    vals = self.get_first_k(node.right, k-len(greater))
                    greater += vals
            elif direction>0 and len(smaller)<k:
                smaller.append(node.val)
                if len(smaller)<k:
                    vals = self.get_last_k(node.left, k-len(smaller))
                    smaller += vals
            
        nearest = [(i, abs(i-target)) for i in smaller+greater]
        nearest.sort(key=operator.itemgetter(1))
        return [item[0] for item in nearest[:k]]
                
    def get_last_k(self, node, k):
        if not node:
            return []
        last_k = self.get_last_k(node.right, k)
        if len(last_k)<k:
            last_k = [node.val]+last_k
        if len(last_k)<k:
            last_k = self.get_last_k(node.left, k-len(last_k))+last_k
        return last_k
        
    def get_first_k(self, node, k):
        if not node:
            return []
        first_k = self.get_first_k(node.left, k)
        if len(first_k)<k:
            first_k = first_k+[node.val]
        if len(first_k)<k:
            first_k = first_k + self.get_first_k(node.right, k-len(first_k))
        return first_k
