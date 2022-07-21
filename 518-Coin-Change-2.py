class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def recur(i,tg):
            if (i,tg) in memo: return memo[(i,tg)]
            if i >= len(coins) or tg < 0:
                return 0
            elif tg == 0:
                return 1
            
            rs = 0
            rs += recur(i, tg-coins[i])
            rs += recur(i+1,tg)
            memo[(i, tg)] = rs
            return rs
        
        bm = recur(0, amount)
        return bm
            