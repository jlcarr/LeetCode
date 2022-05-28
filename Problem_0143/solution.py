# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        # step 1. get length
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        # step 2. cut list in half
        curr = head
        for i in range(l//2-1):
            curr = curr.next
        head2 = curr.next
        curr.next = None
        #print(head,head2)
        
        # step 3. reverse second half
        new_head, new_tail = head2, head2
        while new_tail.next:
            temp = new_tail.next
            new_tail.next = temp.next
            temp.next = new_head
            new_head = temp
        head2 = new_head
        #print(head,head2)
        
        # step 4. weave/merge the lists
        new_head, new_tail = head, head
        head = head.next
        while head2:
            #print(head.val, head2.val)
            new_tail.next = head2
            new_tail = new_tail.next
            head2 = head2.next

            if head:
                new_tail.next = head
                new_tail = new_tail.next
                head = head.next
                
        # step 5 return
        return new_head
