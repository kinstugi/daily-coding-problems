from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b_mp = [0] * 26
        for word in words2:
            k = [0] * 26
            for ch in word:
                k[ord(ch)-ord('a')] += 1
            
            for i in range(26):
                b_mp[i] = max(b_mp[i], k[i])
        
        ans = []
        for word in words1:
            key = [0] * 26
            for ch in word:
                key[ord(ch)-ord('a')] += 1
            
            is_match = True
            for i in range(26):
                if key[i] < b_mp[i]:
                    is_match = False
                    break
            if is_match:
                ans.append(word)
        return ans