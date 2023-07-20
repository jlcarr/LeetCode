class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            if a < 0:
                while result and result[-1] > 0 and result[-1] < -a:
                    result.pop()
                if result and result[-1] == -a:
                    result.pop()
                elif not (result and result[-1] > 0):
                    result.append(a)
            else:
                result.append(a)
        return result
