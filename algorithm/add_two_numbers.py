class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_string = ''
        while l1 is not None:
            l1_string += str(l1.val)
            l1 = l1.next
        l1_string = l1_string[::-1]
        l2_string = ''
        while l2 is not None:
            l2_string += str(l2.val)
            l2 = l2.next
        l2_string = l2_string[::-1]
        result = str(int(l1_string) + int(l2_string))[::-1]
        result = list(map(int, str(result)))
        l3 = ListNode()
        res = l3
        for i in range(len(result)):
            l3.val = result[i]
            if i == len(result) - 1:
                break
            l3.next = ListNode()
            l3 = l3.next
        return res
