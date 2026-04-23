"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # NN=Node()
        # curr=head
        # leng=0
        # while curr:
        #     leng+=1
        #     curr=curr.next
        # we got the length
        # we need the index, we can store the index as a list values
        # l=[[0,0]]*(leng+1)
        # we make the list because we need to know wehre to point
        # for (a,b) in head:
        #     l[a]=head.val
        #     we can use the random pointer to get the index of the list
        #     head=head.next
        # we get a list which have the values, the list 
        # represent the values of ll and also the indexes are there
        # Then we can make a new ll, using this list and we can make a new ll

        # while l:
        #     NN.val=l[j][0]
        #     NN.next=l[j+1][0]
        #     NN.random=l[j][1]
        # return NN

        if not head:
            return None
        mapping={}

        curr=head
        while curr:
            mapping[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            copy=mapping[curr]
            if curr.next:
                copy.next=mapping[curr.next]
            if curr.random:
                copy.random=mapping[curr.random]
            curr=curr.next
        return mapping[head]






        