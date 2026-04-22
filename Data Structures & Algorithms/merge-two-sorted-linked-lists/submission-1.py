# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        # While both lists have nodes
        while list1 and list2:
            if list1.val == list2.val:
                # Attach list1's node
                current.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                # Attach list1's node
                current.next = list1
                list1 = list1.next
            else:
                # Attach list2's node
                current.next = list2
                list2 = list2.next
            # Move current pointer forward
            current = current.next
        
        # Attach whatever remains (one list might be longer)
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list (skip dummy node)
        return dummy.next


          
        