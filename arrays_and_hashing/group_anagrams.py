import collections
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char_s in s:
                arr[ord(char_s) - ord('a')] +=1            
            ans[tuple(arr)].append(s)
            
        return ans.values()
                
                