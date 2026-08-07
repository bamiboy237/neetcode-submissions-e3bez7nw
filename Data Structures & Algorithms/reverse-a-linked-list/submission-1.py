# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 -> 1 -> 2 -> 3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        current = head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev
        