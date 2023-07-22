class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        P = dict()
        P[(row,column)] = 1.
        for move in range(k):
            Pnew = dict()
            for (r,c),p in P.items():
                for rnew,cnew in [
                    (r-2,c-1), (r-2,c+1), 
                    (r-1,c-2), (r-1,c+2),
                    (r+1,c-2), (r+1,c+2),
                    (r+2,c-1), (r+2,c+1)]:
                    if (0 <= rnew <= n-1) and (0 <= cnew <= n-1):
                        if (rnew,cnew) not in Pnew:
                            Pnew[(rnew,cnew)] = 0
                        Pnew[(rnew,cnew)] += p / 8.
            P = Pnew
        return sum(P.values())
