# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            head = list2
        elif not list2:
            head = list1
        else:
            head = list1 if list1.val < list2.val else list2
        
        curr = None
        while list1 and list2:
            #print("curr", curr.val if curr else curr)
            if list1.val < list2.val:
                if curr:
                    curr.next = list1
                    curr = curr.next
                else:
                    curr = list1
                list1 = list1.next
            else:
                if curr:
                    curr.next = list2
                    curr = curr.next
                else:
                    curr = list2
                list2 = list2.next
        if list1:
            if curr:
                curr.next = list1
            else:
                curr = list1
        if list2:
            if curr:
                curr.next = list2
            else:
                curr = list2
        return head
