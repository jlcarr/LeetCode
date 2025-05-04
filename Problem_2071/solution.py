import bisect
from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def check(target_overlap):
            curr_pills = pills
            q = deque()
            i_workers = len(workers) - 1
            for i_tasks in range(target_overlap - 1, -1, -1):
                while i_workers >= len(workers) - target_overlap \
                    and workers[i_workers] + strength >= tasks[i_tasks]:
                    q.append(workers[i_workers])
                    i_workers -= 1
                
                if not q:
                    return True

                if q[0] >= tasks[i_tasks]:
                    q.popleft()
                else:
                    q.pop()
                    curr_pills -= 1
                    if curr_pills < 0:
                        return True
            return False

        #print(list(map(check, range(len(tasks)+1))))
        maxlen = min(len(tasks), len(workers)) + 1
        return bisect.bisect(list(range(maxlen)), False, key=check) - 1
