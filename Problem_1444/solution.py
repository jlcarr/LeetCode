from functools import cache
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows = len(pizza)
        cols = len(pizza[0])

        acc = [[0]*(cols+1)]
        for r in pizza:
            acc_row = []
            count = 0
            for c in r:
                acc_row.append(count)
                count += int(c == 'A')
            acc_row.append(count)
            acc.append(acc_row)
        for c in range(cols+1):
            acc_col = 0
            for r in range(rows+1):
                acc_col += acc[r][c]
                acc[r][c] = acc_col

        #print(acc)

        @cache
        def dp(x,y,krem):
            #print(x,y,krem)
            rem = acc[-1][-1] + acc[y][x] - acc[-1][x] - acc[y][-1]
            if krem == 0:
                #print(x,y, rem)
                return int(rem > 0)
            result = 0
            # v cuts
            for xp in range(x+1,cols):
                remp = acc[-1][-1] + acc[y][xp] - acc[-1][xp] - acc[y][-1]
                if rem - remp > 0:
                    #if dp(xp,y,krem-1) > 0:
                    #    print((x,y), '->', (xp,y), rem - remp, dp(xp,y,krem-1))
                    result = (result + dp(xp,y,krem-1)) % (10**9 + 7)
            # h cuts
            for yp in range(y+1,rows):
                remp = acc[-1][-1] + acc[yp][x] - acc[-1][x] - acc[yp][-1]
                if rem - remp > 0:
                    #if dp(x,yp,krem-1) > 0:
                    #    print((x,y), '->', (x,yp), rem - remp, dp(x,yp,krem-1))
                    result = (result + dp(x,yp,krem-1)) % (10**9 + 7)
            return result

        return dp(0,0,k-1)
