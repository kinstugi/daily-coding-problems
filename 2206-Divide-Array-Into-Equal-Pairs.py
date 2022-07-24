class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp and mp[num] > 0:
                mp[num] -= 1
            else:
                mp[num] = mp.get(num, 0) + 1
        
        print(mp)
        for k,v in mp.items():
            if v > 0:
                return False
        return True