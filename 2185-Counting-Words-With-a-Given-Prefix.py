class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        def isPrefix(prefix, word):
            if len(prefix) > len(word): return False    
            for i in range(len(prefix)):
                if prefix[i] != word[i]: return False
            return True
        
        cnt = 0
        for word in words:
            if isPrefix(pref, word):
                cnt += 1
        
        return cnt