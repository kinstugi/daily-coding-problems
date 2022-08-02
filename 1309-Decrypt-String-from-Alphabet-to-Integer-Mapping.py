from collections import deque

class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp = {str(i): chr(ord('a') + i - 1) for i in range(1, 27)}
    
        ans = ""
        tmp = deque()
        
        for i, ch in enumerate(s):
            if ch == "#":
                while len(tmp) > 2:
                    ans += mp[tmp.popleft()]
                a = tmp.popleft() + tmp.popleft()
                ans += mp[a]
                continue
            tmp.append(ch)
        
        while tmp:
            ans += mp[tmp.popleft()]
        return ans
            
            
                