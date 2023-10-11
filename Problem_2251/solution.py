import heapq
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        endtimes = []
        flowers.sort(reverse=True)

        peopleq = sorted([(t,i) for i,t in enumerate(people)])
        n = len(people)
        answer = [0] * n
        for t,i in peopleq:
            while flowers and flowers[-1][0] <= t:
                heapq.heappush(endtimes, flowers.pop()[-1])
            while endtimes and endtimes[0] < t:
                heapq.heappop(endtimes)
            answer[i] = len(endtimes)
        
        return answer
