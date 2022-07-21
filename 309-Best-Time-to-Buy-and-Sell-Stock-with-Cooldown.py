class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def recur(i, buying):
            if i >= len(prices):
                return 0
            elif (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = recur(i+1, buying)
            
            if buying:
                buy = recur(i+1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = recur(i+2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]
        
        return recur(0, True)