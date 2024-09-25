class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        trie = dict()
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {'COUNT':0}
                curr = curr[c]
                curr['COUNT'] += 1

        result = []
        for word in words:
            count = 0
            curr = trie
            for c in word:
                curr = curr[c]
                count += curr['COUNT']
            result.append(count)
        
        return result
