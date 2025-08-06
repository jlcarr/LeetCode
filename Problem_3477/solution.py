class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    baskets[i] = 0
                    break
        return sum(b > 0 for b in baskets)
