class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Inorder:
    def inorderTraversal(self, root):
        inOrder = []
        self.Traverse(root, inOrder)
        return inOrder
    def Traverse(self, node, inOrder):
        if node:
            self.Traverse(node.left, inOrder)
            inOrder.append(node.val)
            self.Traverse(node.right, inOrder)

obj = Inorder()
root = TreeNode(1)   #root
root.left = TreeNode(2, TreeNode(4), TreeNode(5))    #left subtree
root.right = TreeNode(3, TreeNode(6), TreeNode(7))   #right subtree
print(obj.inorderTraversal(root))



#        visualize tree
#
#               1
#             /   \
#           2       3
#         /  \     /  \
#        4    5   6    7
#
