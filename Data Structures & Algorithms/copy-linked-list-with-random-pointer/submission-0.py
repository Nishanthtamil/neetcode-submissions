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
        if not head:
            return None
        old_to_new={}
        curr=head
        while curr:
            old_to_new[curr]=Node(curr.val)
            curr=curr.next

        curr=head
        while curr:
            new=old_to_new[curr]
            if curr.next:
                new.next=old_to_new[curr.next]
            else:
                new.next=None
            if curr.random:
                new.random=old_to_new[curr.random]
            else:
                new.random=None
            curr=curr.next
        return old_to_new[head]