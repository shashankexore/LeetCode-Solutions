class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            nonlocal ans
            ans = max(ans, l + r)
            return 1 + max(l, r)

        ans = 0
        dfs(root)
        return ans
