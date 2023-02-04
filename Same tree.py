class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        res = self.Traverse(p, q)
        return res

    def Traverse(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2:
            if node1.val == node2.val:
                return self.Traverse(node1.left, node2.left) and self.Traverse(node1.right, node2.right)
            else:
                return False

o = Solution()
p = TreeNode(1,TreeNode(2),TreeNode(3))
q = TreeNode(1,TreeNode(2),TreeNode(3))
print(o.isSameTree(p, q))
