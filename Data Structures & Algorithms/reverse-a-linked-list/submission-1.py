# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# save prev node, curr node, and temp
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init prev and curr pointer
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev points to curr

        return prev

