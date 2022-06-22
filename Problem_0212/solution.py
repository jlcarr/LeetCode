from collections import Counter
class TrieNode:
    def __init__(self):
        self.cs = dict()
        self.is_leaf = False
        
    def add(self, word):
        if not word:
            self.is_leaf = True
            return
        c,word = word[0],word[1:]
        if c not in self.cs:
            self.cs[c] = TrieNode()
        self.cs[c].add(word)
        
    def print(self,prefix=""):
        if self.is_leaf:
            print(prefix)
        for c,v in self.cs.items():
            v.print(prefix=prefix+c)
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board:
            return []
        m,n = len(board), len(board[0])
        
        # setup Trie
        alphabet = Counter([c for row in board for c in row])
        t = TrieNode()
        for word in words:
            if Counter(word) <= alphabet:
                t.add(word)
                #print(word)
        #t.print()
        
        
        # define dfs
        def dfs(t, curr, searched=set()):
            searched = searched | {curr}
            ic,jc = curr
            letter = board[ic][jc]
            t = t.cs[letter]
            
            result = []
            for ix,jx in [(0,1), (0,-1), (1,0), (-1,0)]:
                i,j = ic+ix, jc+jx
                if (0 <= i < m) and (0 <= j < n) \
                    and (i,j) not in searched:
                    c = board[i][j]
                    if c in t.cs:
                        new_curr = (i,j)
                        result += dfs(t, new_curr, searched=searched)
                        if not t.cs[c].is_leaf and len(t.cs[c].cs) == 0:
                            del t.cs[c]
                        
            if t.is_leaf:
                result.append("")
                t.is_leaf = False
            result = [letter+word for word in result]
            #print(result, t.is_leaf)
            return result
        
        # perform search, dfs
        sol = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in t.cs:
                    start = (i,j)
                    sol += dfs(t, start)
        #print('post')
        #t.print()
        return list(set(sol))
