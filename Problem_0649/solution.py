class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # there seems to be no advantage to delaying: one should get rid of the next member.
        Ds = senate.count('D')
        Rs = senate.count('R')
        R_bans, D_bans = 0,0
        while Ds > 0 and Rs > 0:
            new_senate = ''
            for senator in senate:
                if senator == 'D':
                    if D_bans > 0:
                        D_bans -= 1
                    else:
                        R_bans += 1
                        Rs -= 1
                        new_senate += 'D'
                if senator == 'R':
                    if R_bans > 0:
                        R_bans -= 1
                    else:
                        D_bans += 1
                        Ds -= 1
                        new_senate += 'R'
                if Ds == 0 or Rs == 0:
                    break
            senate = new_senate
        if Ds > 0:
            return "Dire"
        return "Radiant"
