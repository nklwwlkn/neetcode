from collections import Counter

class Solution:
    def contains_duplicate(self, nums):
        counter = Counter(nums)
        
        return len(counter) != len(nums)