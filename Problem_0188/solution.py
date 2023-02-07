from functools import cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #vs = []
        @cache
        def rec(i, k, holding):
            # end case
            if i == len(prices):
                return 0
            # pass
            sub_sol = rec(i+1, k, holding)

            if k > 0:
                # transact
                if holding: # sell
                    sub_sol = max(sub_sol, prices[i] + rec(i+1, k-1, not holding))
                else: # buy
                    sub_sol = max(sub_sol, -prices[i] + rec(i+1, k, not holding))
            
            #print((i, k, holding), sub_sol)
            #vs.append(((i, k, holding), sub_sol))
            return sub_sol
        result = rec(0, k, False)
        #for l in sorted(vs):
        #    print(l)
        return result
