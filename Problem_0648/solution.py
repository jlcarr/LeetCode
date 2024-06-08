class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # build trie
        trie = dict()
        for word in dictionary:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = dict()
                curr = curr[c]
            curr['END'] = 0
        
        result = []
        for word in sentence.split():
            result.append(word)
            done = True
            curr = trie
            root = ''
            for c in word:
                if c not in curr:
                    break
                root += c
                curr = curr[c]
                if 'END' in curr:
                    result.pop()
                    result.append(root)
                    break
        return ' '.join(result)
