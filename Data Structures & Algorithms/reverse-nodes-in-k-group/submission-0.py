# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First declare dummy node to handle head manipulation
        dummy = ListNode(0, head)
        gruopPrev = dummy

        while True:
            kth = self.getKthNode(gruopPrev, k)
            if not kth:
                break
            gruopNext = kth.next

            prev, curr = kth.next, gruopPrev.next

            while curr != gruopNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = gruopPrev.next
            gruopPrev.next = kth
            gruopPrev = tmp
            
        return dummy.next


    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr