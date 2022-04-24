import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = collections.Counter(ransomNote)
        magazine = collections.Counter(magazine)
        return ransomNote <= magazine
