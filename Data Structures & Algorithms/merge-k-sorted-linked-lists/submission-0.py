# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Step 1: Collect all values with their frequencies
        freq_map = {}
        
        # Traverse all linked lists
        for head in lists:
            current = head
            while current:
                freq_map[current.val] = freq_map.get(current.val, 0) + 1
                current = current.next
        
        # Step 2: Sort the keys (values)
        sorted_values = sorted(freq_map.keys())
        
        # Step 3: Build the new linked list
        dummy = ListNode()
        tail = dummy
        
        for val in sorted_values:
            count = freq_map[val]
            for _ in range(count):
                tail.next = ListNode(val)
                tail = tail.next
        
        return dummy.next
        