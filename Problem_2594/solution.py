import bisect
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # min result s.t.
        # sum int(sqrt(result / r)) >= cars
        l,r = 1,min(ranks)*cars*cars
        while l < r:
            m = (l+r)//2
            if sum(int(sqrt(m/r)) for r in ranks) >= cars:
                r = m
            else:
                l = m + 1
        return l
