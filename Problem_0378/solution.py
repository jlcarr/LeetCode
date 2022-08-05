import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        max_val = matrix[-1][-1]
        start_heap = [(matrix[r][0], r, 0) for r in range(n)]
        heapq.heapify(start_heap)
        curr_k = 0
        while curr_k < k:
            curr_k += 1
            curr_val, r, c = heapq.heappop(start_heap)
            
            val = matrix[r][c+1] if c+1 < n else max_val+1
            heapq.heappush(start_heap, (val, r, c+1))
        
        return curr_val
            
