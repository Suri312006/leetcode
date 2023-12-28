from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        while pointer < len(nums) :
            if nums[pointer] == val:
                del nums[pointer]
                pointer-=1
            pointer +=1
        
        return len(nums)
    
woo = Solution()
thing = [1,2,2,2,5,6,2,8]
print(woo.removeElement(thing, 2))
print(thing)