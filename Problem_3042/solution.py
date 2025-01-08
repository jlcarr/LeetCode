class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        l = len(words)
        result = 0
        for i in range(l):
            for j in range(i+1,l):
                result += words[j].startswith(words[i]) and words[j].endswith(words[i])
        return result
