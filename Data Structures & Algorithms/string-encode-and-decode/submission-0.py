class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs: 
            ans = ans + str(len(s)) + "#" + s

        return ans 


    def decode(self, s: str) -> List[str]:
        ans = [] 
        length = ""
        i = 0 
        end = 0

        while i < len(s): 
            if s[i] != "#": 
                length += s[i]
                i += 1
            
            else: 
                i += 1
                length = int(length)
                end = i + length 
                ans.append(s[i:end])
                i = end 
                length = ""

        return ans
                


