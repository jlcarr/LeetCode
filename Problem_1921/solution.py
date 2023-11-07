class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted([(d//s, d%s)  for d,s in zip(dist,speed)])
        result = 0
        curr_time = 0
        for i,(t,rem) in enumerate(times):
            if i > t or (t == i and rem == 0):
                return i
        return len(dist)
