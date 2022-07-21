from collections import Counter
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1: return False
        
        #run canSum for half of total
        target = tot // 2
        mp = Counter(nums)
        
        def recur(tg, memo):
            if tg in memo: return memo[tg]
            if tg == 0:
                return True
            elif tg < 0:
                return False
            
            res = False
            for k in mp.keys():
                if mp[k] != 0:
                    mp[k] -= 1
                    res = res or recur(tg-k, memo)
                    mp[k] += 1
            memo[tg] = res
            return res
        
        return recur(target, {})