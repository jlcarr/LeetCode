from collections import Counter
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # for each point, subtract from all others, then lowest terms for the slope
        result = 0
        found = Counter() # (mx, my, yint_x, yint_y)
        n = len(points)
        for i in range(n):
            x1, y1  = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                mx, my = x2-x1, y2-y1

                if mx < 0:
                    mx = -mx
                    my = -my

                # slope in lowest terms
                if mx == 0:
                    found[(0, 1, x1, 0)] += 1
                    continue
                if my == 0:
                    found[(1, 0, 0, y1)] += 1
                    continue

                d = math.gcd(mx, my)
                mx //= d
                my //= d

                # closest positive x to yintercept
                yint_x = ((x1 % mx) + mx) % mx
                yint_dist = (x1 - yint_x) // mx
                yint_y = y1 - my * yint_dist

                # add to the count
                found[(mx, my, yint_x, yint_y)] += 1
            
            print(found)
            most_common = found.most_common(1)
            if not most_common:
                continue
            best_key,best = most_common[0]
            result = max(result, best)
            found.clear()

        return result+1
