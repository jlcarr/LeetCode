class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        tot = 0
        cumsum = [tot := tot + int(c == 'Y') for c in customers]
        minval = (0) + (tot)
        imin = 0
        for i,c in enumerate(cumsum):
            if (i+1 - c) + (tot-c) < minval:
                minval = (i+1 - c) + (tot-c)
                imin = i + 1
        return imin
