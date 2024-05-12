from functools import cmp_to_key
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # q1, q2 -> max(q2/q1*w1, w2)
        # w1/q1 >  w2/q2
        cmp = cmp_to_key(lambda x,y: y[0]*x[1]-x[0]*y[1])
        workers = sorted(zip(quality, wage), key=cmp)
        qual_q = []
        tot_q = 0
        result_num, result_denom = sum(quality) * max(wage), min(quality)
        for q,w in workers:
            tot_q += q
            heapq.heappush(qual_q, -q)
            if len(qual_q) > k:
                tot_q +=  heapq.heappop(qual_q)
            if len(qual_q) == k and tot_q * w * result_denom < result_num * q:
                result_num = tot_q * w
                result_denom = q
            #print((q,w), tot_q, qual_q, result_num, result_denom, result_num/result_denom)
        return result_num / result_denom
