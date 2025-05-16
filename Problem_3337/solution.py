class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7

        counts = [[0] for i in range(26)]
        for c in s:
            counts[ord(c)-ord('a')][0] += 1
        
        matrix = [[int((j < i <= j + nums[j]) or (j < i + 26 <= j + nums[j])) for j in range(26)] for i in range(26)]
        
        def matmul(ml, mr):
            return [[sum(ml[i][k] * mr[k][j] % mod for k in range(len(mr))) for j in range(len(mr[0]))] for i in range(len(ml))]

        def matpow(m, p):
            if p == 1:
                return m
            if p % 2 == 0:
                m2 = matpow(m, p//2)
                return matmul(m2, m2)
            return matmul(matpow(m, p-1), m)

        #for row in matrix:
        #    print(row)
        return sum([row[0] for row in matmul(matpow(matrix, t), counts)]) % mod
