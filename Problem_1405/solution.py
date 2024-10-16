import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = [(-a,'a'),(-b,'b'),(-c,'c')]
        heapq.heapify(q)
        cooldown = None
        result = []
        while q:
            count,v = heapq.heappop(q)
            if count == 0:
                continue
            if cooldown is not None:
                heapq.heappush(q, cooldown)
            if not q:
                result.append(v * min(2, -count))
                return ''.join(result)
            used = 1
            if -count >= 2 - q[0][0]:
                used = 2
            result.append(v * used)
            count -= -used
            cooldown = (count, v)
        return ''.join(result)
