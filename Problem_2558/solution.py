import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            v = -heapq.heappop(gifts)
            leave = int(math.sqrt(v))
            heapq.heappush(gifts, -leave)
            #print(i,v,leave, v-leave)
        return -sum(gifts)
