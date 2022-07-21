class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def recur(i, tg):
            if (i, tg) in memo: return memo[(i,tg)]
            if i >= len(nums):
                if tg == target: return 1
                return 0    
            rs = 0
            rs += recur(i+1, tg + nums[i])
            rs += recur(i+1, tg - nums[i])
            memo[(i, tg)] = rs
            return rs
        return recur(0,0)