import heapq
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        counts = dict()
        queue = []
        curr = 0
        curr_sum = 0
        while curr < amount:
            for c in coins:
                new_target = c + curr
                if new_target > amount:
                    break
                if new_target not in counts:
                    counts[new_target] = 1 + curr_sum
                    heapq.heappush(queue, new_target)
                else:
                    counts[c+curr] = min(counts[c+curr], 1 + curr_sum)

            if not queue:
                return -1
            curr = heapq.heappop(queue)
            curr_sum = counts.pop(curr)
        
        if curr != amount:
            return -1
        return curr_sum
