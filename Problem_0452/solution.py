class LL:
    def __init__(self, p):
        self.p = p
        self.next = None
        self.prev = None
        
    def remove_self(self):
        if self.prev:
            self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev
        elif self.next:
            self.next.prev = None
        
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # run through sorted by start until first end is reached:
        # all prior starts are eliminated
        # repeat
        points = list(set(map(tuple,points)))
        points.sort(reverse=True)
        
        end_queue_finder = dict()
        end_queue = None
        curr = None
        for p in sorted(points, key=lambda x: x[1]):
            if end_queue is None:
                end_queue = LL(p)
                curr = end_queue
            else:
                curr.next = LL(p)
                curr.next.prev = curr
                curr = curr.next
            end_queue_finder[p] = curr
        
        # while ending overlaps
        result = 0
        while end_queue:
            # get next end
            #print(end_queue.p[1])
            while points and points[-1][0] <= end_queue.p[1]:
                #print(points[-1], end_queue.p[1])
                if points[-1] != end_queue.p:
                    end_queue_finder.pop(points[-1]).remove_self()
                points.pop()
            end_queue = end_queue.next
            result += 1
        return result
            
                
