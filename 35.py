from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        for i in range(len(nums)):
            if nums[i]>target:
                return i 
            
            if i == len(nums)-1:
                return len(nums)

            print(nums[i])
        
        
            
woo = Solution()
lol = [1,3,5,6]

print(woo.searchInsert(lol,7))