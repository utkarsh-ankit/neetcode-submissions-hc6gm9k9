# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def s(l):
            i=1
            k=0
            while l:
                k+=i*l.val
                i*=10
                l=l.next
            return k
        su=s(l1)+s(l2)
        dummy=ListNode()

        cur=dummy
        if su==0:
            return ListNode(0)
        head=None
        while su>0:
            d=su%10
            cur.next=ListNode(d)

            cur=cur.next
            su//=10
        return dummy.next
            
            





        