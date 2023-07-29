class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        # n,n -> 0.25 n-4, n
        #        0.25 n-3, n-1
        #        0.25 n-2, n-2
        #        0.25 n-1, n-3

        # A     B 
        # n-1   1/4 n-3
        # n-2   1/4 n-2, 1/4^2 n-6
        # n-3   1/4 n-1, 1/4^2 n-5, 1/4^2 n-5, 1/4^3 n-9
        # n-3   1/4 n-1, 2/4^2 n-5, 1/4^3 n-9
        # n-4   1/4 n, 2(1/4^2 n-4, 2/4^3 n-8, 1/4^4 n-12), (1/4 n-2, 1/4^2 n-6)^2, 
        # n-4   1/4 n, 2/4^2 n-4, 4/4^3 n-8, 2/4^4 n-12, 1/4^2 n-4, 2/4^3 n-8, 1/4^4 n-12
        # n-4   1/4 n, 3/4^2 n-4, 6/4^3 n-8, 3/4^4 n-12

        # sum {0<= k3 <= n} 0.25^k3 * 0.75^(n-k3) * C(n,k3)
        # 

        if n > 1000:
            return 1.

        max_A = n
        states = {max_A: {n: 1.}}
        #print(states)
        while max_A > 0:
            if max_A not in states:
                max_A -= 1
                continue
            for B,p in states.pop(max_A).items():
                for i in range(4):
                    new_A = max(max_A - 4 + i, 0)
                    new_B = max(B - i, 0)
                    if new_B == 0 and new_A > 0:
                        continue
                    if new_A not in states:
                        states[new_A] = dict()
                    if new_B not in states[new_A]:
                        states[new_A][new_B] = 0
                    states[new_A][new_B] += p / 4.
            max_A -= 1
        #print(states)
        return sum(p for p in states[0].values()) - states[0][0] / 2.
