class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        minvals = [None] * (n+1)
        minvals[0] = 0

        trie = dict()
        for word in dictionary:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr['LEAF'] = True
        
        for i in range(n):
            t_curr = trie
            i_curr = i
            while i_curr < n and s[i_curr] in t_curr:
                t_curr = t_curr[s[i_curr]]
                i_curr += 1
                if 'LEAF' in t_curr:
                    if minvals[i_curr] is None:
                        minvals[i_curr] = minvals[i]
                    minvals[i_curr] = min(minvals[i_curr], minvals[i])
            if minvals[i+1] is None:
                minvals[i+1] = minvals[i]+1
            minvals[i+1] = min(minvals[i+1], minvals[i]+1)
        return minvals[-1]
