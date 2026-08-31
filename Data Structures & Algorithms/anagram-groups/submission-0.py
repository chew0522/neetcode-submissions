class Solution:
    def get_key(self, word): 
        count = [0] * 26 
        for ch in word: 
            count[ord(ch) - ord('a')] += 1
        
        return tuple(count)

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for word in strs:
            key = self.get_key(word)
            ans[key].append(word)

        return list(ans.values())

    

    