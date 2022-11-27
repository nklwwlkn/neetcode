from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        counter = 0

        for num in nums:
            if (num - 1) not in hashmap and num in hashmap:
                i = 1
                while (num + i) in hashmap:
                    i += 1
                counter = max(counter, i)
        
        return counter
