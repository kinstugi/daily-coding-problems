class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        def isPrefix(pref, word):
            if len(pref) > len(word): return False
            for i in range(len(pref)):
                if pref[i] != word[i]: return False
            return True
            
        i = 0
        while s:
            if i == len(words) or not isPrefix(words[i], s): 
                return False
            s = s[len(words[i]):]
            i += 1
            
        return True
                