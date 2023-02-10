class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        res=ListNode(0)
        carry=0
        arr=[]
        while (l1 or l2) and res:
            if l1 and not l2:
                res.val=l1.val
                l1=l1.next
                arr.append(res.val)
            if not l1 and l2:
                res.val=l2.val
                l2=l2.next
                arr.append(res.val)
            if l1 and l2:
                res.val=l1.val+l2.val+carry
                carry=res.val//10
                res.val=res.val%10
                arr.append(res.val)
                l1=l1.next
                l2=l2.next

            res.next=ListNode(0)
            res=res.next
        if carry:
            res.val=carry
            arr.append(res.val)
        return arr

a=Solution()
l1=ListNode(0,ListNode(0,ListNode(0,ListNode(1))))
l2=ListNode(0,ListNode(2,ListNode(3)))
print(a.addTwoNumbers(l1,l2))


#input   3->2->4      423
#        4->5->6      654
#------------------------
#output  7->7->0->1  1077

