class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        memo = {}
        
        def isSubsequence(sub, txt):
            if sub in memo: return memo[sub]
            if len(sub) > len(txt):
                memo[sub] = False
                return False
            
            l = 0
            for i in range(len(txt)):
                if len(sub) == l:
                    break
                if l < len(sub) and txt[i] == sub[l]:
                    l +=1
            memo[sub] = len(sub) == l
            return memo[sub]
        
        cnt = 0
        for word in words:
            if isSubsequence(word, s):
                cnt += 1
        
        return cnt