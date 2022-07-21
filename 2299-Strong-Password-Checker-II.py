# i guess you can use some form of regex but I could not get my regex to pass all the test case
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        def containsCap(psw):
            for ch in psw:
                if 'A' <= ch <= 'Z': return True
            return False

        def containsLow(psw):
            for ch in psw:
                if 'a' <= ch <= 'z': return True
            return False
        
        def containsNum(psw):
            for ch in psw:
                if '0' <= ch <= '9': return True
            return False
        
        def containsSpec(psw):
            for ch in psw:
                if ch in '!@#$%^&*()-+': return True
            return False
        
        if len(password) < 8: return False
        for i in range(len(password)-1):
            if password[i] == password[i+1]: return False
        
        return containsCap(password) and containsLow(password) and containsNum(password) and containsSpec(password)