# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        temp = None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        if temp:
            temp.next = None
        # while head:
        #     print(head.val)
        #     head = head.next
        # print("xxxxxx")
        # while slow:
        #     print(slow.val)
        #     slow = slow.next
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        list1 = head
        list2 = prev
        # while list1:
        #     print(list1.val)
        #     list1 = list1.next
        # print("=====")
        # while list2:
        #     print(list2.val)
        #     list2 = list2.next

        while list1 and list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1 if temp1 else temp2
            list1, list2 = temp1, temp2

