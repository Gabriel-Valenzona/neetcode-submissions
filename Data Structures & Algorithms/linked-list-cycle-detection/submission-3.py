# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use hashset time and space complexity o(n) to populate the set according to size of linkedlist
        seen = set()
        curr = head
        # if node value is seen in hashset, take advantage of the o(1) access time, then return True
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next 
        
        return False

        

