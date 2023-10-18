import heapq
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # setup graph
        prereqs = {course:[] for course in range(n)}
        precounts = [0]*n
        for prevCourse,nextCourse in relations:
            prereqs[prevCourse-1].append(nextCourse-1)
            precounts[nextCourse-1] += 1
        
        # intialize q
        q = []
        for course,count in enumerate(precounts):
            if count == 0:
                heapq.heappush(q, (time[course], course))
        
        # run
        t = 0
        while q:
            t = q[0][0]
            while q and q[0][0] == t:
                t, course = heapq.heappop(q)
                for nextCourse in prereqs[course]:
                    precounts[nextCourse] -= 1
                    if precounts[nextCourse] == 0:
                        heapq.heappush(q, (t+time[nextCourse], nextCourse))
        return t
        
            
