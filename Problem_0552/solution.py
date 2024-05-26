import numpy as np
class Solution:
    def checkRecord(self, n: int) -> int:
        self.mod = 10**9 + 7
        T = np.zeros((6,6), dtype=int)
        for A in range(2):
            for L in range(3):
                # present (resets lates)
                T[A*3, A*3 + L] = 1
                # late (adds to lates if valid)
                if L < 2:
                    T[A*3 + L + 1, A*3 + L] = 1
                # absent (reset lates if valud)
                if A < 1:
                    T[(A+1)*3, A*3 + L] = 1
        def matpowmod(A,n):
            if n == 1:
                return A
            if n % 2 == 0:
                return np.linalg.matrix_power(matpowmod(A,n//2), 2) % self.mod
            return np.matmul(A, matpowmod(A,n-1)) % self.mod
        #print(T)
        Tpow = matpowmod(T,n)

        return Tpow[:,0].sum() % self.mod
