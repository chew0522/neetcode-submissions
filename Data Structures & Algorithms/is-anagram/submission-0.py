class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        
        sd = {} 

        for ch in s: 
            if ch in sd: 
                sd[ch] += + 1 
            else: 
                sd[ch] = 1
        
        for ch in t: 
            if ch not in sd: 
                return False 
            else: 
                if sd[ch] < 1: return False 

                sd[ch] -= 1 

        return True

        