# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        freq_map={}

        for head in lists:
            current=head
            while current:
                freq_map[current.val]=freq_map.get(current.val,0)+1
                current=current.next
            
        sorted_values=sorted(freq_map.keys())

        dummy=ListNode()
        tail=dummy

        for val in sorted_values:
            count=freq_map[val]
            for _ in range(count):
                tail.next=ListNode(val)
                tail=tail.next
        return dummy.next
        