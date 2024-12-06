import math
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.append(n+1)
        banned.sort()
        result = 0
        acc = 0
        p = 0
        for i in banned:
            if p >= n:
                break
            #print(i, p+1, i == p+1)
            if i <= p+1:
                p = i
                continue
            if acc + p+1 > maxSum:
                break
            fullsum = i*(i-1)//2 - p*(p+1)//2
            if fullsum + acc <= maxSum:
                acc += fullsum
                result += i-1 - p
                #print('at fullsum', i)
                #print('added', p+1, 'to', i-1, 'sum', fullsum, 'count', i-1 - p)
                #print('total sum of', acc, 'count', result)
                p = i
                continue
            # max_{j <= i, j*(j-1)/2 - p*(p+1)/2 + acc <= maxSum}
            # (1/2)*j*j - (1/2)*j - p*(p+1)/2 + acc - maxSum <= 0
            # j <= (1/2) +- sqrt(1/4 + p*(p+1) + 2*(maxSum-acc))
            # j <= (1 +- sqrt(1 + 4*p*(p+1) + 8*(maxSum-acc)))/2
            j = int((1 + math.sqrt(1 + 4*p*(p+1) + 8*(maxSum-acc)))//2)
            j = min(j, i)
            acc += j*(j-1)//2 - p*(p+1)//2
            result += j-1 - p
            #print('at partial', i)
            #print('added', p+1, 'to', j-1, 'sum', j*(j-1)//2 - p*(p+1)//2, 'count', j-1 - p)
            #print('total sum of ', acc, 'count', result)
            break
        return result
