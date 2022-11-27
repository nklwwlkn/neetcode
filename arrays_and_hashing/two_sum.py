from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        hashmap = {}
        
        for idx, num in enumerate(nums):
            hashmap[num] = idx
            

        for idx, num in enumerate(nums):
            lookup = target - num
            
            if hashmap.get(lookup) and hashmap.get(lookup) != idx:
                return [hashmap.get(lookup), idx]
        
        
            
            
        