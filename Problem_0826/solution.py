class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        jobq = sorted(zip(difficulty, profit), reverse=True)
        maxprofit = 0
        result = 0
        for ability in worker:
            while jobq and ability >= jobq[-1][0]:
                maxprofit = max(maxprofit, jobq.pop()[-1])
            result += maxprofit
        
        return result
