class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = len(s1)
        
        off_count = 0
        c_counts = [0]*26
        for c in s1:
            n = ord(c)-ord('a')
            if c_counts[n] == 0:
                off_count += 1
            c_counts[n] -= 1
        
        for i in range(len(s2)):
            # dropping off
            if i >= l:
                n = ord(s2[i-l])-ord('a')
                if c_counts[n] == 0:
                    off_count += 1
                c_counts[n] -= 1
                if c_counts[n] == 0:
                    off_count -= 1
            # jumping in
            n = ord(s2[i])-ord('a')
            if c_counts[n] == 0:
                off_count += 1
            c_counts[n] += 1
            if c_counts[n] == 0:
                off_count -= 1
            
            # check solution
            if off_count == 0:
                return True
        
        return False
