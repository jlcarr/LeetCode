import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = set([-1,len(nums)])
        q = [(v,i) for i,v in enumerate(nums)]
        heapq.heapify(q)
        while len(marked)-2 < len(nums):
            v,i = heapq.heappop(q)
            score += v
            marked.add(i)
            marked.add(i-1)
            marked.add(i+1)
            while q and q[0][1] in marked:
                heapq.heappop(q)
        return score
