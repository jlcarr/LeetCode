class WordDictionary:

    def __init__(self):
        self.vals = dict()
        self.is_leaf = False

    def addWord(self, word: str) -> None:
        if not word:
            self.is_leaf = True
        else:
            c, word = word[0], word[1:]
            if c not in self.vals:
                self.vals[c] = WordDictionary()
            self.vals[c].addWord(word)

    def search(self, word: str) -> bool:
        if not word:
            return self.is_leaf
        else:
            c, word = word[0], word[1:]
            if c == '.':
                for v in self.vals.values():
                    if v.search(word):
                        return True
                return False
            else:
                if c not in self.vals:
                    return False
                return self.vals[c].search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
