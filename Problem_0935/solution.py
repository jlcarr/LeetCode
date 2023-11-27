class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        moves = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [2,4],
        }

        p = [1] * 10
        for i in range(n-1):
            pp = [0]*10
            for k,v in moves.items():
                for k2 in v:
                    pp[k2] = (pp[k2] + p[k]) % mod
            p = pp
        
        return sum(p) % mod
            
