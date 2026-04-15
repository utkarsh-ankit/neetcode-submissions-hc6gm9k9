class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def i(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            i(root.left)
            i(root.right)
            return root
        return i(root)