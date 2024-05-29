class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l,r = 0,0
        cost = 0
        result = 0
        while r < len(s):
            cost += abs(ord(s[r])-ord(t[r]))
            if cost <= maxCost:
                result = max(result, r+1-l)
            while cost <= maxCost and r < len(s)-1:
                r += 1
                cost += abs(ord(s[r])-ord(t[r]))
                #print(l,r, cost)
                if cost <= maxCost:
                    result = max(result, r+1-l)
            while cost > maxCost and l < r:
                cost -= abs(ord(s[l])-ord(t[l]))
                l += 1
            #print(l,r, cost)
            if cost <= maxCost:
                result = max(result, r+1-l)
            r += 1
        return result
            

