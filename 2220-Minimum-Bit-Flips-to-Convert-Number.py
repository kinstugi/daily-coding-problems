class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = goal ^ start
        cnt = 0
        while res:
            cnt += res & 1
            res >>= 1
        return cnt