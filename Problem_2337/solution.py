class Solution:
    def canChange(self, start: str, target: str) -> bool:
        L_needed = 0
        R_excess = 0
        for cs,ct in zip(start,target):
            if cs == 'L':
                L_needed -= 1
            elif cs == 'R':
                R_excess += 1
                if L_needed > 0:
                    return False

            if ct == 'L':
                L_needed += 1
                if R_excess > 0:
                    return False
            elif ct == 'R':
                R_excess -= 1

            if L_needed < 0 or R_excess < 0:
                return False
        if L_needed != 0 or R_excess != 0:
                return False
        return True
