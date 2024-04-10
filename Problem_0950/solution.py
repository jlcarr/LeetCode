from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        l = len(deck)
        indices = deque(list(range(l)))
        order = []
        while indices:
            order.append(indices.popleft())
            if indices:
                indices.append(indices.popleft())
        result = [0] * l
        for i_val, val in zip(order,deck):
            result[i_val] = val
        return result
