import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        pigs = int(math.log(buckets)/math.log(tests+1))
        return pigs if buckets <= (tests+1)**pigs else pigs+1
        # if tests == 1
        # buckets -> {pigs}
        # 1 -> {}
        # 2 -> {0}
        # 3 -> {1}
        # 4 -> {0,1}
        # 5 -> {2}
        # 6 -> {0,2}
        # 7 -> {1,2}
        # 8 -> {0,1,2}
        # nbuckets <= 2**npigs
        #nbuckets <= (tests+1)**npigs
        # if tests == 2
        # 1 -> {}
        # 2 -> {(L):0, (D):1}
        # 3 -> {(L):{(L):0, (D):2}, (D):1}
        # 4 ->
        # ({1}):
        # (L):
        #     ({2}):
        #     (L):
        #         0
        #     (D):
        #         2
        # (D):
        #     1
        # Tot: 3

        # ({1,3},{2,3})
        # (L,L):
        #     ({4,6},{5,6}):
        #     (L,L):
        #         ({0})
        #     (D,L):
        #         ({4})
        #     (L,D):
        #         ({5})
        #     (D,D):
        #         ({6})
        # (D,L):
        #     1
        # (L,D):
        #     2
        # (D,D):
        #     3
        # Tot: 7

