class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.trie['LEAF'] = len(words)-1 # empty suffix and prefix technically matches the largest word
        for index,w in enumerate(words): 
            for offset in range(len(w)): # run through the offset strings
                suffpref = w[offset:] + '-' + w
                curr_node = self.trie #inserting them into the trie
                for c in suffpref:
                    if c not in curr_node:
                        curr_node[c] = dict()
                    curr_node = curr_node[c]
                    curr_node['LEAF'] = index
            

    def f(self, pref: str, suff: str) -> int:
        curr_node = self.trie
        for c in suff + '-' + pref:
            if c not in curr_node:
                return -1
            curr_node = curr_node[c]
        return curr_node['LEAF']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
