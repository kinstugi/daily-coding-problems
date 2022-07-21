class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        def recur(tg, memo):
            if tg in memo: return memo[tg]
            if tg == "":
                return True
            res = False
            for word in wordDict:
                if tg.find(word) == 0:
                    res = res or recur(tg[len(word):], memo)
            memo[tg] = res
            return res
        
        return recur(s, {})