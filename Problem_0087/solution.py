from functools import cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        
        @cache
        def search(start1, start2, l):
            #print('F', start1, start2, l)
            if l == 1:
                return s1[start1] == s2[start2]
                
            left1, left2, right2_swapped = set(), set(), set()
            for i in range(1,l):
                left1.add(s1[start1+i-1])
                left2.add(s2[start2+i-1])
                right2_swapped.add(s2[start2+l-i])
                
                if left1 == left2:
                    if search(start1, start2, i) and search(start1+i, start2+i, l-i):
                        return True
                if left1 == right2_swapped:
                    if search(start1, start2+l-i, i) and search(start1+i, start2, l-i):
                        return True
            return False
        
        return search(0, 0, len(s1))
