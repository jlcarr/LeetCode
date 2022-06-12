class Trie:

    def __init__(self):
        self.leaf = False
        self.vals = dict()

    def insert(self, word: str) -> None:
        if word == "":
            self.leaf = True
        else:
            c,word = word[0],word[1:]
            if c not in self.vals:
                self.vals[c] = Trie()
            self.vals[c].insert(word)

    def search(self, word: str) -> bool:
        if word:
            c,word = word[0],word[1:]
            if c not in self.vals:
                return False
            return self.vals[c].search(word)
        else:
            return self.leaf

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            c,prefix = prefix[0],prefix[1:]
            if c not in self.vals:
                return False
            return self.vals[c].startsWith(prefix)
        else:
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
