from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_q = [(-count,task) for task,count in Counter(tasks).items()]
        heapq.heapify(task_q)
        cooldown_q = deque([])
        
        t = 0
        while task_q or cooldown_q:
            while cooldown_q and cooldown_q[-1][0] <= t:
                t_cooldown, count, task  = cooldown_q.pop()
                heapq.heappush(task_q, (count, task))
            
            if task_q:
                count, task = heapq.heappop(task_q)
            else:
                t_cooldown, count, task  = cooldown_q.pop()
                #print(f"{t}: idle x{t_cooldown-t}")
                t = t_cooldown
            count += 1
            #print(f"{t+1}: {task}, rem:{-count}")
            if count < 0:
                cooldown_q.appendleft((t+1+n, count, task))
            t += 1
                
        return t
