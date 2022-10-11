class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        
        longest_word = ''
        buildable = set([''])
        for w in words:
            if w[:-1] in buildable:
                buildable.add(w)
                if len(w) > len(longest_word):
                    longest_word = w
                
        return longest_word
