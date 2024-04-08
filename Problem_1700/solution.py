from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        l_students = len(students)
        l_sandwiches = len(sandwiches)
        sandwiches = sandwiches[::-1]
        while sandwiches:
            new_students = []
            for student in students:
                if student == sandwiches[-1]:
                    sandwiches.pop()
                else:
                    new_students.append(student)
            if len(new_students) == l_students and len(sandwiches) == l_sandwiches:
                return len(new_students)
            l_students = len(new_students) 
            l_sandwiches = len(sandwiches)
            students = new_students
        return 0
