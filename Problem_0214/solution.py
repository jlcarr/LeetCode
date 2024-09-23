class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # we don't need to match all the end:
        # we must search for the start
        l = len(s)//2
        table = [-1] * (l+1)
        ipref = 0
        for i in range(1,l):
            if s[i] == s[ipref]:
                table[i] = table[ipref]
            else:
                table[i] = ipref
                while ipref >= 0 and s[i] != s[ipref]:
                    ipref = table[ipref]
            ipref += 1
        table[l] = ipref
        #print(table)

        iend = len(s)-1
        istart = 0
        while iend >= istart:
            if s[istart] == s[iend]:
                istart += 1
                iend -= 1
                if istart > iend: #found
                    #print(istart, iend, s[2*istart - int(istart - iend > 1):][::-1])
                    return s[2*istart - int(istart - iend > 1):][::-1] + s
            else:
                istart = table[istart]
                if istart < 0:
                    istart += 1
                    iend -= 1
        return ''

