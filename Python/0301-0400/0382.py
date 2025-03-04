class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = ans = 0
        head = self.head
        while head:
            n += 1
            x = random.randint(1, n)
            if n == x:
                ans = head.val
            head = head.next
        return ans
