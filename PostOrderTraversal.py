class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Postorder:
    def postorderTraversal(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if node:
            self.traverse(node.left, result)
            self.traverse(node.right, result)
            result.append(node.val)


o = Postorder()
root = TreeNode(1)  # root
root.left = TreeNode(2, TreeNode(4), TreeNode(5))  # left subtree
root.right = TreeNode(3, TreeNode(6), TreeNode(7))  # right subtree
print(o.postorderTraversal(root))

#        visualize tree
#
#               1
#             /   \
#           2       3
#         /  \     /  \
#        4    5   6    7