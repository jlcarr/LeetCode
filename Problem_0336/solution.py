class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # put all words into the trie backwards
        trie = dict()
        back_trie = dict()
        for j,word in enumerate(words):
            w = list(word)
            curr = trie
            for c in w:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr['END'] = j
            curr = back_trie
            while w:
                c = w.pop()
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
                if not w:
                    curr['END'] = j
        import json
        #print(json.dumps(trie, indent=4))
        #print(json.dumps(back_trie, indent=4))

        # for each word i, search the trie for an ending matching the beginning
        result = set()
        for i,word in enumerate(words):
            # forwards
            curr = back_trie
            for index,c in enumerate(word):
                if c not in curr: 
                    break
                if 'END' in curr[c] and curr[c]['END'] != i: # is the rest of word a palindrome?
                    if word[index+1:] == word[-1:index:-1]:
                        result.add((i, curr[c]['END']))
                curr = curr[c]
          # backwards
            curr = trie
            if 'END' in curr and word == word[::-1] and curr['END'] != i: # is the word a palindrome?
                result.add((i, curr['END']))
                result.add((curr['END'], i))
            word = word[::-1]
            for index,c in enumerate(word):
                if c not in curr: 
                    break
                if 'END' in curr[c] and curr[c]['END'] != i: # is the rest of word a palindrome?
                    if word[index+1:] == word[-1:index:-1]:
                        result.add((curr[c]['END'], i))
                curr = curr[c]
        return list(map(list,result))



