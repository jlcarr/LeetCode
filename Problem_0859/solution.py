class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        counts = [0]*26
        mismatches = 0
        mismatched = set()
        mismatchedg = set()
        for c,cg in zip(s,goal):
            if c != cg:
                mismatches += 1
                if mismatches > 2:
                    return False
                mismatched.add(c)
                mismatchedg.add(cg)
            else:
                counts[ord(c)-ord('a')] += 1
        if mismatches == 2 and mismatched == mismatchedg:
            return True
        if mismatches == 0:
            return max(counts) >= 2
        return False
