class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(x, d):
            nonlocal maxDepth, s, ws
            maxDepth = max(maxDepth, d)
            if x.isInteger():
                s += x.getInteger()
                ws += x.getInteger() * d
            else:
                for y in x.getList():
                    dfs(y, d + 1)

        maxDepth = s = ws = 0
        for x in nestedList:
            dfs(x, 1)
        return (maxDepth + 1) * s - ws
