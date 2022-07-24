class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subs = []
        ans = [0]
        
        def xor_total(arr):
            if not arr: return 0
            n = arr[0]
            for i in range(1, len(arr)):
                n ^= arr[i]
            return n
        
        def recur(i):
            if i >= len(nums):
                ans[0] += xor_total(subs[:])
                return
            
            subs.append(nums[i])
            recur(i+1)
            subs.pop()
            
            recur(i+1)
        
        recur(0)
        return ans[0]