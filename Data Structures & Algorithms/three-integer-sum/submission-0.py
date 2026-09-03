class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        i = 0
        while i < len(nums): 
            j, k = i+1, len(nums) - 1
            while j < k: 
                if j == i: 
                    j += 1
                elif k == i: 
                    k -= 1
                x = nums[i] + nums[j] + nums[k]
                if x == 0: 
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1 
                    k -= 1
                elif x < 0: 
                    j += 1
                else: 
                    k -= 1
            
            i += 1
    
        return [list(a) for a in ans]
