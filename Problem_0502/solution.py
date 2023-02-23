import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        notpossible = list(zip(capital,profits))
        possible = []
        heapq.heapify(notpossible)
        #print(w, notpossible, possible)
        for i in range(k):
            while notpossible and notpossible[0][0] <= w:
                c,p = heapq.heappop(notpossible)
                heapq.heappush(possible, -p)
            if possible:
                w -= heapq.heappop(possible)
            #print(w, notpossible, possible)
        return w
