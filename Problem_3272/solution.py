from collections import Counter
import math
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        result = 0
        hset = set()
        mids = [''] if n % 2 == 0 else list(map(str,range(10)))
        r = range(10**(n//2-1), 10**(n//2)) if n > 1 else ['']
        for m in mids:
            for i in r:
                #print(i)
                if i != '':
                    i = str(i)
                i = i + m + i[::-1]
                if i == '0':
                    continue
                #print(i)
                #print()
                i_sorted = int(''.join(sorted(i, reverse=True)))
                if i_sorted in hset or int(i) % k != 0:
                    continue
                hset.add(i_sorted)
                counts = Counter(i)
                subresult = math.factorial(n)
                for c in counts.values():
                    subresult //= math.factorial(c)
                if '0' in counts:
                    leading0 = math.factorial(n-1)
                    counts['0'] -= 1
                    for c in counts.values():
                        leading0 //= math.factorial(c)
                    subresult -= leading0
                result += subresult
        return result
                
