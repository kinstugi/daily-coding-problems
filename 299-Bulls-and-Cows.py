class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        b_set = Counter(secret)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                b_set[secret[i]] -= 1
        
        for i,c in enumerate(guess):
            if c != secret[i] and c in b_set and b_set[c] > 0:
                cows += 1
                b_set[c] -= 1
        
        return f"{bulls}A{cows}B"
            