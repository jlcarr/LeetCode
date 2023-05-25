class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n-k > maxPts:
            return 1.

        p = [0.] * (n+1)
        p[0] = 1.

        window_p = 1.
        for i in range(1,n+1):
            p[i] = window_p / maxPts # equally likely to get probability from anywhere in window
            if i < k: # update the window to include this term now 
                window_p += p[i]
            if i - maxPts >=0: # a term has fallen out of the window
                window_p -= p[i-maxPts]


        return sum(p[k:])
