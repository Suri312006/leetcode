from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        counter = 1
        length = len(nums)
        while counter < length:
           if nums[counter-1] == nums[counter]:
               del nums[counter]
               counter-=1
               length-=1
           
           counter+=127
        
        return length
    
woo = Solution()
thing = [-1,0,0,0,0,3,3]


woo.removeDuplicates(thing)

print(thing)