class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root is None:
            return root

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        else:
            return self.searchBST(root.right, val)