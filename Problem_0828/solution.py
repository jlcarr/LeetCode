class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = 0
        for c in set(s):
            #print(c, 'START')
            # count all the substrings in which it appears once
            prev = -1
            prev_streak = 0 # includes finishing index
            i = 0
            while i < len(s): # for the entire string
                while i < len(s) and s[i] != c: # find the next index of interest
                    i += 1
                if i == len(s):
                    break
                # count up everything excluding the found index
                # choose anything after the prev times anything before the prev including
                result += (i - prev) * prev_streak
                #print(c, i, result)
                #print(prev, prev_streak, "+", (i - prev) * prev_streak)
                prev_streak = i-prev
                prev = i
                i += 1
            result += (i - prev) * prev_streak
            #print(c, i, result, 'END')
            #print(prev, prev_streak, '+', (i - prev) * prev_streak)
        return result
            
