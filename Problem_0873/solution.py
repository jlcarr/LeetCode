class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        p = dict()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                vi, vj = arr[i], arr[j]
                p[(vi,vj)] = 1 + p.get((vj - vi, vi), 1)
        #print(p)
        result = max(p.values())
        if result <= 2:
            return 0
        return result

