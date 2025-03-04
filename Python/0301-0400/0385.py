class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s or s == '[]':
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        ans = NestedInteger()
        depth, j = 0, 1
        for i in range(1, len(s)):
            if depth == 0 and (s[i] == ',' or i == len(s) - 1):
                ans.add(self.deserialize(s[j:i]))
                j = i + 1
            elif s[i] == '[':
                depth += 1
            elif s[i] == ']':
                depth -= 1
        return ans
