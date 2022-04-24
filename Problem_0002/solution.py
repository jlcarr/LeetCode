# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = l1
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry
            carry = l1.val//10
            l1.val %= 10
            l1_tail = l1
            l1,l2 = l1.next, l2.next
        if l2:
            l1 = l1_tail
            l1.next = l2
            l1 = l1.next
        while l1:
            l1.val += carry
            carry = l1.val//10
            l1.val %= 10
            l1_tail = l1
            l1 = l1.next
        if carry:
            l1_tail.next = ListNode(val=carry)
            
        return result
