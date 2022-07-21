class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = [c for c in s]
        def shift(ch, num):
            return chr(ord(ch) + num)
        for i in range(1, len(s), 2):
            arr[i] = shift(s[i-1], int(s[i]))
        
        return "".join(arr)