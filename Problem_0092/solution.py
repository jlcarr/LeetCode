# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = None
        left_node = head
        for i in range(left-1):
            prev = left_node
            left_node = left_node.next
        
        swaps = right - left
        new_right_node = left_node
        new_left_node = left_node
        for i in range(swaps):
            temp = new_right_node.next
            new_right_node.next = temp.next
            temp.next = new_left_node
            new_left_node = temp
        
        if prev:
            prev.next = new_left_node
            return head
        else:
            return new_left_node
        
