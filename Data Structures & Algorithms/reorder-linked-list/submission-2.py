# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_midpoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        # 4 -> 5 -> 6 -> 7
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        midpoint = self.find_midpoint(head)
        second = midpoint.next
        midpoint.next = None
        reversed_ = self.reverse_list(second)

        first = head

        while first and reversed_:
            first_next = first.next
            reversed_next = reversed_.next

            first.next = reversed_
            reversed_.next = first_next

            first = first_next
            reversed_ = reversed_next