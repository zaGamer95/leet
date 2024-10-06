# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = ListNode()
        current = t
        carry = 0

        while l1 or l2 or carry:
            sum_val = carry
            # print(sum_val)
            # print(l1)
            # print(l2)
            # print(carry)
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        return t.next