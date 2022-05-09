import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sol = None
        t_count = collections.Counter(t)
        rem = len(t)
        j = 0
        for i in range(len(s)):
            #print(i,j, s[j:i+1], t_count)
            c = s[i]
            if c in t_count:
                t_count[c] -= 1
                if t_count[c] >= 0:
                    rem -= 1
            if rem == 0: # check if a solution has been found
                while j < i+1:
                    #print(i,j, s[j:i+1], t_count)
                    c = s[j]
                    if c in t_count:
                        if t_count[c] == 0:
                            break
                        t_count[c] += 1
                    j += 1
                if not sol or sol[1]-sol[0] > 1+i-j:
                    sol = (j, 1+i)
        if not sol:
            return ""
        return s[sol[0]:sol[1]]
        
