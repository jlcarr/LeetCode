"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = None
        if not head:
            return None
        # fill with indices
        curr = head
        i = 0
        while curr:
            curr.index = i
            curr = curr.next
            i += 1

        # first pass for the base list and construct the dict
        value_map = dict()
        result_curr = None
        curr = head
        while curr:
            if result is None:
                result = Node(x=curr.val)
                result_curr = result
            else:
                result_curr.next = Node(x=curr.val)
                result_curr = result_curr.next
            value_map[curr.index] = result_curr
            curr = curr.next

        # fill in the random values
        curr = head
        while curr:
            if curr.random:
                value_map[curr.index].random = value_map[curr.random.index]
            curr = curr.next

        return result
