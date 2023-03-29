class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        acc = 0
        cumsum = []
        for s in satisfaction:
            acc += s
            cumsum.append(acc)
        
        result = sum((t+1)*s for t,s in enumerate(satisfaction))
        t = 1
        for i,s in enumerate(satisfaction):
            if s >= 0:
                break
            if -s*t - (cumsum[-1] - cumsum[i]) > 0:
                result += -s*t - (cumsum[-1] - cumsum[i])
                #print(f"remove {s} at time {t}")
            else:
                #print(f"keep {s} at time {t}")
                t += 1
        return result
