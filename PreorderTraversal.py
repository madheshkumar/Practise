class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Preorder:
    def preorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if node:
            result.append(node.val)
            self.traverse(node.left, result)
            self.traverse(node.right, result)


o = Preorder()
root = TreeNode(1)  # root
root.left = TreeNode(2, TreeNode(4), TreeNode(5))  # left subtree
root.right = TreeNode(3, TreeNode(6), TreeNode(7))  # right subtree
print(o.preorderTraversal(root))

#        visualize tree
#
#               1
#             /   \
#           2       3
#         /  \     /  \
#        4    5   6    7
#
