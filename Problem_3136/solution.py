class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not all(
            (ord('A') <= ord(c) <= ord('Z')) or 
            (ord('a') <= ord(c) <= ord('z')) or 
            (ord('0') <= ord(c) <= ord('9')) for c in word):
            return False
        if not any(
            (c in 'aeiou') or
            (c in 'AEIOU')
            for c in word):
            return False
        if not any(
            ((ord('a') <= ord(c) <= ord('z')) and (c not in 'aeiou')) or
            ((ord('A') <= ord(c) <= ord('Z')) and (c not in 'AEIOU'))
            for c in word):
            return False
        return True
