class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = list(enumerate([sum(r) for r in mat]))
        argsort = sorted(mat, key=lambda x: x[1])
        return [x[0] for x in argsort[:k]]
