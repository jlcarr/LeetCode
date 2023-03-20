class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if sum(flowerbed[0:2]) == 0:
            n -= 1
            flowerbed[0] = 1
            if n == 0:
                return True
        for i in range(1, len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2]) == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        if len(flowerbed) >= 2 and  flowerbed[-1]+flowerbed[-2] == 0:
            n -= 1
            flowerbed[-1] = 1
            if n == 0:
                return True
        return False
