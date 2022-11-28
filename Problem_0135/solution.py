class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sol = [1]*n
        if n == 1:
            return 1
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                sol[i] = max(sol[i], sol[i-1]+1)

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                sol[i] = max(sol[i], sol[i+1]+1)
        
        return sum(sol)
