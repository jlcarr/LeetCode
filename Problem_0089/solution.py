class Solution:
    def grayCode(self, n: int) -> List[int]:
        def rec(n):
            if n == 0:
                return ['']
            sub = rec(n-1)
            return ["0"+v for v in sub] + ["1"+v for v in sub[::-1]]
        return [int(v,2) for v in rec(n)]
