import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        u = [1]
        idxs = [0] * len(primes)
        heap = [(v, i) for (i,v) in enumerate(primes)]
        
        while len(u)!=n:
            newu, _ = heap[0]
            u.append(newu)
            while heap[0][0]==newu:
                _, i = heapq.heappop(heap)
                idxs[i]+=1
                heapq.heappush(heap, (u[idxs[i]]*primes[i], i))
        
            # print newu, heap
        return u[-1]
            
            
