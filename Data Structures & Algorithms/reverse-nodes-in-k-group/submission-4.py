
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # a=0
        # curr=head
        # unc=1
        # while curr:
        #     a+=1
        #     curr=curr.next
        # if (2*k)<a:
        #     unc=a%(2*k)

        # def rev(node):
        #     prev=0
        #     while node:
        #         temp=node.next
        #         node.next=prev
        #         prev=node
        #         node=temp
        #     return node

        # curr=head
        # for i in range(2*k):
        #     i+=1
        #     b=unc//(i*k)
        #     while b:
        #         curr=curr.next
        #         rev(curr)
        # return curr

        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next

        dummy=ListNode(0)
        dummy.next=head
        prev_group_end=dummy
        curr=head

        for _ in range(count//k):
            group_start=curr
            prev=None

            for _ in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp

            prev_group_end.next=prev
            group_start.next=curr
            prev_group_end = group_start
        
        return dummy.next
