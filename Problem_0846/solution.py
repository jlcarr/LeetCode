from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        q = deque()
        active = 0
        prev = -2
        counts = Counter(hand)
        for i, (card,count) in enumerate(sorted(counts.items())):
            #print(q, i, card, prev, count, active)
            if q and i - q[-1][0] == groupSize:
                active -= q.pop()[1]
            if card != prev+1 and active>0: # consecutive broken
                return False
            if count < active: # not enough to cover groups
                return False
            if count > active: # new group
                q.appendleft((i,count-active))
                active += count-active
            prev = card
        if q and i - q[-1][0] >= groupSize:
                active -= q.pop()[1]
        #print(active)
        return len(q) == 1 and len(counts) - q[-1][0] == groupSize

