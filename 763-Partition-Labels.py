class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        mp = {}
        for i,c in enumerate(s):
            mp[c] = i
            
        sz = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, mp[c])
            sz += 1
            
            if i == end:
                ans.append(sz)
                sz = 0
        return ans
                