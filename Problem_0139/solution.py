import heapq

class Trie:
    def __init__(self):
        self.vals = dict()
        
    def add(self, word):
        curr = self.vals
        for c in word:
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        curr[None] = None
        
    def isin(self, word):
        curr = self.vals
        for c in word:
            if c not in curr:
                return False
        return None in curr
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
            
        reacheables = [0]
        reached = set(reacheables)
        while reacheables:
            start_i = heapq.heappop(reacheables)
            i = start_i
            curr = trie.vals
            while i < len(s) and s[i] in curr:
                curr = curr[s[i]]
                i += 1
                if None in curr:
                    if i == len(s):
                        return True
                    if i not in reached:
                        heapq.heappush(reacheables, i)
                        reached.add(i)
        
        return False
        
