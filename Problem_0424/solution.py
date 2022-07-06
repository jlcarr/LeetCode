class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for c in set(s):
            l = 0
            # deal with invalid situation
            while k == 0 and l < len(s) and s[l] != c:
                l += 1
            if l == len(s):
                continue
                
            curr_k = k - int(s[l] != c)
            r = l
            result = max(result, r-l+1)
            #print(c)
            while r+1 < len(s):
                #print(r,l, curr_k)
                # first try to move r up
                if s[r+1] == c:
                    r += 1
                    result = max(result, r-l+1)
                elif curr_k > 0:
                    curr_k -= 1
                    r += 1
                    result = max(result, r-l+1)
                else:
                    # otherwise move up l
                    if s[l] == c:
                        l += 1 
                    else: # if l wasn't on a c
                        curr_k += 1
                        l += 1
                    if l > r:
                        if s[l] != c:
                            curr_k -= 1
                        while k == 0 and l < len(s) and s[l] != c:
                            l += 1
                        r = l
        return result
                
