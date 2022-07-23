from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.palindrome_indices = dict()
        for i in range(len(s)):
            # try odd palindromes
            l = 0
            while i-l >= 0 and i+l < len(s) and s[i-l] == s[i+l]:
                if i-l not in self.palindrome_indices:
                    self.palindrome_indices[i-l] = []
                self.palindrome_indices[i-l].append(i+l)
                l += 1
            # try even palindromes
            l = 0
            while i-l >= 0 and i+1+l < len(s) and s[i-l] == s[i+1+l]:
                if i-l not in self.palindrome_indices:
                    self.palindrome_indices[i-l] = []
                self.palindrome_indices[i-l].append(i+1+l)
                l += 1
        
        #print(self.palindrome_indices)
        
        @cache
        def rec(i):
            if i == len(s):
                return [[]]
            result = []
            for end in self.palindrome_indices[i]:
                result += [ [s[i:end+1]] + partition for partition in rec(end+1)]
            #print(i, result, self.palindrome_indices[i], s[i:])
            return result
        
        
        return rec(0)
    

