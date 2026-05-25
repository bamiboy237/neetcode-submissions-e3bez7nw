# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = []
        curr_node = head
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next

        target = len(stack) - n + 1

        #remove node

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        i = 1
        while curr:
            if i == target:
                prev.next = curr.next
                break
            else:
                i += 1
                prev = curr
                curr = curr.next
        return dummy.next
            
            
