class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {} 
        bucket = [[] for i in range(len(nums) + 1)]
        ans = []

        for num in nums: 
            if num in seen: 
                seen[num] += 1
            else: 
                seen[num] = 1 

        for num, count in seen.items(): 
            bucket[count].append(num) 
        
        for i in range(len(nums), 0, -1): 
            if bucket[i]: 
                for item in bucket[i]:
                    ans.append(item)
            
            if len(ans) == k: 
                return ans 
        
        return ans
                
        
        