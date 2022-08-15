import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        taken_courses = []
        curr_end = 0
        for duration, lastDay in courses:
            curr_end += duration
            heapq.heappush(taken_courses, -duration)
            
            while curr_end > lastDay:
                curr_end += heapq.heappop(taken_courses)
        
        return len(taken_courses)
