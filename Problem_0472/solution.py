class Trie:
    def __init__(self, root=None):
        self.branches = dict()
        self.is_leaf = False
        self.root = self
        if root:
            self.root = root
    
    def __repr__(self, t=0):
        result = ""
        for k,v in self.branches.items():
            result += " "*t + f"{k}({self.is_leaf}):\n"
            result += v.__repr__(t=t+1)
        return result
        
    def insert(self, w):
        if not w:
            self.is_leaf = True
            return
        c, w = w[0], w[1:]
        if c not in self.branches:
            self.branches[c] = Trie(root=self.root)
        self.branches[c].insert(w)
        
    def search_concat(self, w):
        if not w:
            return self.is_leaf
        if self.is_leaf and self.root.search_concat(w):
            return True
        c, w = w[0], w[1:]
        if c not in self.branches:
            return False
        return self.branches[c].search_concat(w)
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))
        result = []
        t = Trie()
        for w in words:
            if t.search_concat(w):
                result.append(w)
            t.insert(w)
        #print(t)
        return result
