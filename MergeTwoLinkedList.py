class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        if list1.val < list2.val:
            seek, target = list1, list2
        else:
            seek, target = list2, list1
        head = seek

        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next

        return head


list1=ListNode(1,ListNode(2,ListNode(4)))
list2=ListNode(1,ListNode(3,ListNode(4)))
a=Solution()
print(a.mergeTwoLists(list1,list2))