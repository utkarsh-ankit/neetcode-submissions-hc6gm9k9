# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        curr=head
        t=head
        while curr:
            i+=1
            curr=curr.next
        if i==n:
            return head.next
        k=i-n-1
        while k>0:
            t=t.next
            k-=1
        t.next=t.next.next
        return head        