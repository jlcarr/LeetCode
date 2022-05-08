from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i,j):
            # match is good
            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                return dp(i+1,j+1)
            elif i == len(word1): # must add all letters
                return len(word2) - j
            elif j == len(word2): # must delete all remaining letters
                return len(word1) - i
            return 1 + min(
                dp(i,j+1), # insert a matching letter
                dp(i+1,j), # delete a letter
                dp(i+1,j+1) #replace the letter to match
            )
        
        return dp(0,0)
