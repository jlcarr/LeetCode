class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # initial to effectively inf
        n = 365+1
        minCosts = [sum(costs)*n]*n
        minCosts[0] = 0
        curr = 0
        for day in range(1,n):
            if curr < len(days) and day == days[curr]:
                minCosts[day] = min(minCosts[day], minCosts[day-1] + costs[0])
                for forward in range(7):
                    if day+forward >= n:
                        break
                    minCosts[day+forward] = \
                    min(minCosts[day+forward], minCosts[day-1] + costs[1])
                for forward in range(30):
                    if day+forward >= n:
                        break
                    minCosts[day+forward] = \
                    min(minCosts[day+forward], minCosts[day-1] + costs[2])
                curr += 1
            else:
                minCosts[day] = min(minCosts[day], minCosts[day-1])
        return minCosts[-1]
