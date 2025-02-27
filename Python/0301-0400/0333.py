class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return inf, -inf, 0
            lmi, lmx, ln = dfs(root.left)
            rmi, rmx, rn = dfs(root.right)
            nonlocal ans
            if lmx < root.val < rmi:
                ans = max(ans, ln + rn + 1)
                return min(lmi, root.val), max(rmx, root.val), ln + rn + 1
            return -inf, inf, 0

        ans = 0
        dfs(root)
        return ans
