class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        res=ListNode()
        temp=res
        carry=0
        arr=[]
        while l1 or l2 or carry:
            val=carry
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            carry=val//10
            val=val%10
            arr.append(val)
            temp.next=ListNode(val)
            temp=temp.next
        return res.next,arr

a=Solution()
l1=ListNode(0,ListNode(0,ListNode(0,ListNode(1))))
l2=ListNode(0,ListNode(2,ListNode(3)))
print(a.addTwoNumbers(l1,l2))



#input   3->2->4      423
#        4->5->6      654
#------------------------
#output  7->7->0->1  1077

