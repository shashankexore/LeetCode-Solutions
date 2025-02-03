class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def buildBST(nums, start, end):
            if start > end:
                return None
            mid = (start + end) >> 1
            return TreeNode(
                nums[mid], buildBST(nums, start, mid - 1), buildBST(nums, mid + 1, end)
            )

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return buildBST(nums, 0, len(nums) - 1)
