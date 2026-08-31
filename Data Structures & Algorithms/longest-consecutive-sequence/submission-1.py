class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        global_con = 0
        num_set = set(nums)

        for i, num in enumerate(num_set): 
            local_con = 1
            if num-1 not in num_set: 
                while num+local_con in num_set: 
                    local_con += 1
                if local_con > global_con: 
                    global_con = local_con


        return global_con


