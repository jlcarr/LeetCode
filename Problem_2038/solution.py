class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        As = 0
        Bs = 0
        prev2 = None
        prev1 = None
        for c in colors:
            if c == prev1 and c == prev2:
                if c == 'A':
                    As += 1
                if c == 'B':
                    Bs += 1
            prev2 = prev1
            prev1 = c
        

        return As > Bs
