# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()
        prev.next = l1
        carry = 0
        while l1 and l2:
            l1.val += + l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            prev.next = l2
        while carry > 0:
            if prev.next:
                prev.next.val += carry
                carry = prev.next.val // 10
                prev.next.val %= 10
                prev = prev.next
            else:
                prev.next = ListNode(carry)
                carry = 0
        return dummy.next