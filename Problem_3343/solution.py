from collections import Counter
from functools import cache
import math

# ans = perm(odds) * perm(evens)
# for each selection of odd digits, num perms:
# ans = (n_odd_digits!)*(n_even_digits!)/prod_i (n_even_i!) * (n_odd_i!)
# dp(i, rem, target)

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        target = sum(int(d) for d in num) 
        if target % 2 == 1:
            return 0
        target //= 2

        mod = 10**9 + 7
        l = len(num)
        total_perm = math.factorial(l//2) * math.factorial(l//2+(l%2)) % mod

        counts = Counter(list(map(int,num)))
        kcounts = sorted(counts.keys())
        vcounts = [counts[k] for k in kcounts]
        #print(kcounts)
        #print(vcounts)

        @cache
        def dp(i, rem, target):
            if rem == 0:
                return (target == 0) * total_perm * pow(math.prod(map(math.factorial, vcounts[i:])), -1, mod) % mod
            if i == len(kcounts) or target < 0:
                return 0
            result = 0
            for itake in range(min(rem, vcounts[i])+1):
                #print(i+1, rem-itake, target - kcounts[i]*itake, '->', sub, sub // math.factorial(itake) // math.factorial(vcounts[i] - itake), math.factorial(itake),  math.factorial(vcounts[i] - itake))
                result += dp(i+1, rem-itake, target - kcounts[i]*itake) * pow(math.factorial(itake) * math.factorial(vcounts[i] - itake), -1, mod) % mod
            return result
            
        return dp(0, l//2, target) % mod

        # 028899
        # 288 099
        # perm(001) = 001, 010, 100
        # 3 * 3 * 2

        # 2 * (3!)*(3!) // 2! // 2!

