from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum([anscount + (ans + 1 - anscount) % (ans + 1) if ans+1 < anscount else ans+1 for ans,anscount in Counter(answers).items()])
        # if ans+1 > anscount -> 1 color, not all polled, ans+1 tot
        # if ans+1 = anscount -> 1 color, all polled, ans+1 tot
        # if ans+1 < anscount -> >1 color, 
        # anscount + (ans + 1 - anscount) % (ans + 1)
        # 1,1,1
        # 2 < 3
        # 0,3 1,2
