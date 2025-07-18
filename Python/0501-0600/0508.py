class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            s = l + r + root.val
            cnt[s] += 1
            return s

        cnt = Counter()
        dfs(root)
        mx = max(cnt.values())
        return [k for k, v in cnt.items() if v == mx]
