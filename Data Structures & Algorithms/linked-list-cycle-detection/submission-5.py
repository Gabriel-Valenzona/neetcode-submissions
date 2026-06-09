# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # init fast and slow pointers - floyd's algorithm
        slow, fast = head, head
        # idea is: if there is a cycle, then eventually the fast pointer will be at the same node 
        # as the slow pointer on an iteration
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False



        

        

