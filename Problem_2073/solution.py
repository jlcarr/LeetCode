class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        v = tickets[k]
        return sum([min(t,v-int(i > k)) for i,t in enumerate(tickets)])
