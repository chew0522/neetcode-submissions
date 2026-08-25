class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {} 

        for num in nums: 
            if num in seen: 
                seen[num] += 1
            else: 
                seen[num] = 1
        
        ans = sorted(seen, key=lambda k: seen[k], reverse=True)

        return ans[:k] 